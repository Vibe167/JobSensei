"""
ML Career Predictor - Integration with New XGBoost Model
Uses the trained model from ML Model folder
"""

import numpy as np
import pickle
import json
import os
from sentence_transformers import SentenceTransformer

class MLCareerPredictor:
    def __init__(self, model_path="ML Model/ML Model/model_artifacts"):
        """Initialize the ML model and load artifacts"""
        print("🔄 Loading ML Career Prediction Model...")
        
        try:
            self.model = pickle.load(open(f"{model_path}/career_model.pkl", "rb"))
            self.le_career = pickle.load(open(f"{model_path}/career_encoder.pkl", "rb"))
            self.scaler = pickle.load(open(f"{model_path}/scaler.pkl", "rb"))
            self.cat_encoders = pickle.load(open(f"{model_path}/cat_encoders.pkl", "rb"))
            
            with open(f"{model_path}/metrics.json") as f:
                self.metrics = json.load(f)
            with open(f"{model_path}/metrics_per_career.json") as f:
                self.per_career = json.load(f)
            with open(f"{model_path}/career_skills_reference.json") as f:
                self.skills_ref = json.load(f)
            with open(f"{model_path}/feature_info.json") as f:
                self.feat_info = json.load(f)
            
            self.sbert = SentenceTransformer('all-MiniLM-L6-v2')
            print("✅ ML Model loaded successfully!")
            print(f"   Model: {self.metrics['model']}")
            print(f"   Accuracy: {self.metrics['overall_metrics']['accuracy']:.2%}")
            print(f"   Careers: {len(self.le_career.classes_)}")
            
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            raise
    
    def build_features(self, quiz_answers):
        """
        Build feature vector from quiz answers
        
        Args:
            quiz_answers: dict with keys Q1-Q25
        
        Returns:
            numpy array of features
        """
        # Numeric features (Q1-Q10)
        numeric = [
            float(quiz_answers.get('Q1_realistic', 3)),
            float(quiz_answers.get('Q2_investigative', 3)),
            float(quiz_answers.get('Q3_artistic', 3)),
            float(quiz_answers.get('Q4_social', 3)),
            float(quiz_answers.get('Q5_enterprising', 3)),
            float(quiz_answers.get('Q6_conventional', 3)),
            float(quiz_answers.get('Q7_math', 3)),
            float(quiz_answers.get('Q8_communication', 3)),
            float(quiz_answers.get('Q9_technical', 3)),
            float(quiz_answers.get('Q10_design', 3))
        ]
        
        # Categorical features (Q11-Q22)
        cat_vals = {
            'Q11_work_env': quiz_answers.get('Q11_work_env', 'Flexible'),
            'Q12_team_size': quiz_answers.get('Q12_team_size', 'Small (2-5)'),
            'Q13_risk': quiz_answers.get('Q13_risk', 'Medium'),
            'Q14_pace': quiz_answers.get('Q14_pace', 'Moderate'),
            'Q15_values': quiz_answers.get('Q15_values', 'Making impact'),
            'Q16_prefers': quiz_answers.get('Q16_prefers', 'Mix of all'),
            'Q17_balance': quiz_answers.get('Q17_balance', 'Very'),
            'Q18_education': quiz_answers.get('Q18_education', 'Bachelors'),
            'Q19_subjects': quiz_answers.get('Q19_subjects', 'Mixed'),
            'Q20_coding': quiz_answers.get('Q20_coding', 'Basic'),
            'Q21_indoor': quiz_answers.get('Q21_indoor', 'Mostly indoor'),
            'Q22_age': quiz_answers.get('Q22_age', '23-27'),
        }
        
        encoded = []
        for col, val in cat_vals.items():
            le = self.cat_encoders.get(col)
            try:
                encoded.append(int(le.transform([str(val)])[0]))
            except:
                encoded.append(0)  # Default for unknown values
        
        # Text features (Q23-Q25) - SBERT embeddings
        text = f"Problem I love: {quiz_answers.get('Q23_problem_text', '')} | " \
               f"My dream: {quiz_answers.get('Q24_dream_text', '')} | " \
               f"My best skill: {quiz_answers.get('Q25_skill_text', '')}"
        
        emb = self.sbert.encode([text])[0]
        
        # Combine all features
        return np.hstack([np.array(numeric + encoded), emb]).reshape(1, -1)
    
    def calculate_skill_gap(self, career, quiz_answers):
        """Calculate skill gap for a career"""
        required = self.skills_ref.get(career, [])
        have = []
        
        # Infer skills from quiz answers
        if float(quiz_answers.get('Q9_technical', 0)) >= 3:
            have += ["Python", "Programming", "Technical Skills", "Coding", "SQL"]
        if float(quiz_answers.get('Q7_math', 0)) >= 3:
            have += ["Mathematics", "Statistics", "Analytical Skills"]
        if float(quiz_answers.get('Q8_communication', 0)) >= 3:
            have += ["Communication", "Writing", "Presentation"]
        if float(quiz_answers.get('Q10_design', 0)) >= 3:
            have += ["Design", "Visual Communication", "Creativity"]
        
        coding_level = quiz_answers.get('Q20_coding', 'Basic')
        if coding_level in ["Intermediate", "Advanced", "Expert"]:
            have += ["Git", "Data Analysis", "Algorithms"]
        
        # Match skills
        have_lower = [h.lower() for h in have]
        matched = [s for s in required if any(h in s.lower() or s.lower() in h for h in have_lower)]
        gap = [s for s in required if s not in matched]
        
        readiness_score = round(len(matched) / len(required) * 100) if required else 50
        
        return {
            "skills_required": required,
            "skills_you_have": matched,
            "skills_gap": gap,
            "readiness_score": readiness_score
        }
    
    def predict(self, quiz_answers, top_n=5):
        """
        Predict top N careers for given quiz answers
        
        Args:
            quiz_answers: dict with quiz responses
            top_n: number of top careers to return
        
        Returns:
            list of career predictions with confidence scores
        """
        try:
            # Build and scale features
            feat = self.build_features(quiz_answers)
            feat_scaled = self.scaler.transform(feat)
            
            # Get predictions
            proba = self.model.predict_proba(feat_scaled)[0]
            top_indices = proba.argsort()[-top_n:][::-1]
            
            results = []
            for rank, idx in enumerate(top_indices, 1):
                career = self.le_career.classes_[idx]
                confidence = round(float(proba[idx]) * 100, 1)
                
                # Get career metrics
                cm = self.per_career.get(career, {})
                
                # Calculate skill gap
                sg = self.calculate_skill_gap(career, quiz_answers)
                
                results.append({
                    "rank": rank,
                    "career": career,
                    "ml_confidence": confidence,
                    "model_metrics": {
                        "precision": cm.get("precision", 0),
                        "recall": cm.get("recall", 0),
                        "f1_score": cm.get("f1_score", 0)
                    },
                    "skills_required": sg["skills_required"],
                    "skills_you_have": sg["skills_you_have"],
                    "skills_gap": sg["skills_gap"],
                    "readiness_score": sg["readiness_score"],
                    "data_source": "O*NET v28.2 (US Dept of Labor) + BLS OEWS 2024"
                })
            
            return {
                "success": True,
                "top_careers": results,
                "model_info": {
                    "algorithm": "XGBoost Classifier",
                    "text_processing": "SBERT all-MiniLM-L6-v2 (384-dim embeddings)",
                    "training_data": "O*NET v28.2 + BLS OEWS 2024",
                    "overall_f1": self.metrics["overall_metrics"]["f1_score"],
                    "overall_precision": self.metrics["overall_metrics"]["precision"],
                    "overall_recall": self.metrics["overall_metrics"]["recall"],
                    "overall_accuracy": self.metrics["overall_metrics"]["accuracy"]
                }
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "top_careers": []
            }
    
    def get_all_careers(self):
        """Get list of all supported careers"""
        return list(self.le_career.classes_)
    
    def get_model_info(self):
        """Get detailed model information"""
        return {
            "model": self.metrics["model"],
            "problem": f"Multi-class Classification ({len(self.le_career.classes_)} careers)",
            "data_sources": [
                {"name": "O*NET v28.2", "org": "US Dept of Labor", "url": "https://www.onetcenter.org"},
                {"name": "BLS OEWS 2024", "org": "Bureau of Labor Statistics", "url": "https://www.bls.gov/oes/"}
            ],
            "input_processing": {
                "mcq": "22 features via LabelEncoder + StandardScaler",
                "text": "SBERT all-MiniLM-L6-v2 → 384-dim semantic embeddings",
                "total": self.feat_info["total_features"] + 384
            },
            "performance": self.metrics["overall_metrics"],
            "cross_validation": self.metrics["cross_validation"],
            "careers": list(self.le_career.classes_)
        }


# Example usage
if __name__ == "__main__":
    # Initialize predictor
    predictor = MLCareerPredictor()
    
    # Example quiz answers
    sample_answers = {
        'Q1_realistic': 4,
        'Q2_investigative': 5,
        'Q3_artistic': 2,
        'Q4_social': 3,
        'Q5_enterprising': 3,
        'Q6_conventional': 2,
        'Q7_math': 5,
        'Q8_communication': 4,
        'Q9_technical': 5,
        'Q10_design': 2,
        'Q11_work_env': 'Flexible',
        'Q12_team_size': 'Small (2-5)',
        'Q13_risk': 'High',
        'Q14_pace': 'Fast',
        'Q15_values': 'Innovation',
        'Q16_prefers': 'Technical work',
        'Q17_balance': 'Very',
        'Q18_education': 'Bachelors',
        'Q19_subjects': 'STEM',
        'Q20_coding': 'Advanced',
        'Q21_indoor': 'Mostly indoor',
        'Q22_age': '23-27',
        'Q23_problem_text': 'Building AI systems that solve real-world problems',
        'Q24_dream_text': 'Lead an AI research team at a top tech company',
        'Q25_skill_text': 'Machine learning and deep learning implementation'
    }
    
    # Get predictions
    result = predictor.predict(sample_answers, top_n=5)
    
    if result["success"]:
        print("\n" + "="*60)
        print("TOP 5 CAREER PREDICTIONS")
        print("="*60)
        for career in result["top_careers"]:
            print(f"\n{career['rank']}. {career['career']}")
            print(f"   Confidence: {career['ml_confidence']}%")
            print(f"   Readiness: {career['readiness_score']}%")
            print(f"   Skills Gap: {len(career['skills_gap'])} skills needed")
    else:
        print(f"Error: {result['error']}")
