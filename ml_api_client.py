"""
ML API Client - Connects Flask app to FastAPI ML Model
Communicates with the XGBoost + SBERT model running on port 8000
"""

import requests
from typing import Dict, List, Optional
import json

class MLAPIClient:
    """Client to communicate with the FastAPI ML model server"""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.is_available = self._check_availability()
    
    def _check_availability(self) -> bool:
        """Check if ML API server is running"""
        try:
            response = requests.get(f"{self.base_url}/", timeout=2)
            return response.status_code == 200
        except:
            return False
    
    def predict_career(self, quiz_data: Dict) -> Optional[Dict]:
        """
        Send quiz answers to ML model and get career predictions
        
        Args:
            quiz_data: Dictionary containing all quiz answers (Q1-Q25)
        
        Returns:
            Dictionary with top 5 career predictions and details
        """
        if not self.is_available:
            print("⚠️  ML API server not available. Please start it with:")
            print("   cd 'ML Model/ML Model' && python -m uvicorn fastapi_server:app --reload --port 8000")
            return None
        
        try:
            # Prepare payload for API
            payload = self._prepare_payload(quiz_data)
            
            # Make prediction request
            response = requests.post(
                f"{self.base_url}/predict",
                json=payload,
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"❌ ML API error: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"❌ Error calling ML API: {e}")
            return None
    
    def _prepare_payload(self, quiz_data: Dict) -> Dict:
        """Convert quiz data to ML API format"""
        
        # Map numeric questions (Q1-Q10) - these are 1-5 scale
        payload = {
            "Q1_realistic": float(quiz_data.get("Q1", 3)),
            "Q2_investigative": float(quiz_data.get("Q2", 3)),
            "Q3_artistic": float(quiz_data.get("Q3", 3)),
            "Q4_social": float(quiz_data.get("Q4", 3)),
            "Q5_enterprising": float(quiz_data.get("Q5", 3)),
            "Q6_conventional": float(quiz_data.get("Q6", 3)),
            "Q7_math": float(quiz_data.get("Q7", 3)),
            "Q8_communication": float(quiz_data.get("Q8", 3)),
            "Q9_technical": float(quiz_data.get("Q9", 3)),
            "Q10_design": float(quiz_data.get("Q10", 3)),
        }
        
        # Map categorical questions (Q11-Q22)
        payload.update({
            "Q11_work_env": quiz_data.get("Q11_work_env", "Flexible"),
            "Q12_team_size": quiz_data.get("Q12_team_size", "Small (2-5)"),
            "Q13_risk": quiz_data.get("Q13_risk", "Medium"),
            "Q14_pace": quiz_data.get("Q14_pace", "Moderate"),
            "Q15_values": quiz_data.get("Q15_values", "Making impact"),
            "Q16_prefers": quiz_data.get("Q16_prefers", "Mix of all"),
            "Q17_balance": quiz_data.get("Q17_balance", "Very"),
            "Q18_education": quiz_data.get("Q18_education", "Bachelors"),
            "Q19_subjects": quiz_data.get("Q19_subjects", "Mixed"),
            "Q20_coding": quiz_data.get("Q20_coding", "Basic"),
            "Q21_indoor": quiz_data.get("Q21_indoor", "Mostly indoor"),
            "Q22_age": quiz_data.get("Q22_age", "23-27"),
        })
        
        # Map text questions (Q23-Q25) - these use SBERT embeddings
        payload.update({
            "Q23_problem_text": quiz_data.get("Q23_problem_text", ""),
            "Q24_dream_text": quiz_data.get("Q24_dream_text", ""),
            "Q25_skill_text": quiz_data.get("Q25_skill_text", ""),
        })
        
        return payload
    
    def get_model_info(self) -> Optional[Dict]:
        """Get information about the ML model"""
        if not self.is_available:
            return None
        
        try:
            response = requests.get(f"{self.base_url}/model-info", timeout=5)
            if response.status_code == 200:
                return response.json()
        except:
            pass
        return None
    
    def get_metrics(self) -> Optional[Dict]:
        """Get model performance metrics"""
        if not self.is_available:
            return None
        
        try:
            response = requests.get(f"{self.base_url}/metrics", timeout=5)
            if response.status_code == 200:
                return response.json()
        except:
            pass
        return None
    
    def get_supported_careers(self) -> Optional[List[str]]:
        """Get list of all careers the model can predict"""
        if not self.is_available:
            return None
        
        try:
            response = requests.get(f"{self.base_url}/careers", timeout=5)
            if response.status_code == 200:
                data = response.json()
                return data.get("careers", [])
        except:
            pass
        return None


# Singleton instance
_ml_client = None

def get_ml_client() -> MLAPIClient:
    """Get or create ML API client instance"""
    global _ml_client
    if _ml_client is None:
        _ml_client = MLAPIClient()
    return _ml_client
