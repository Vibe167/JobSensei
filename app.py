from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import numpy as np
import pandas as pd
import pickle
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import ML API Client for new XGBoost + SBERT model
from ml_api_client import get_ml_client

# Initialize ML client
ml_client = get_ml_client()

# Check if new ML model is available
if ml_client.is_available:
    print("✅ Using NEW ML model (XGBoost + SBERT all-MiniLM-L6-v2) via FastAPI")
    print("   Model running at: http://localhost:8000")
    model_info = ml_client.get_model_info()
    if model_info:
        print(f"   F1 Score: {model_info['performance']['f1_score']}")
        print(f"   Precision: {model_info['performance']['precision']}")
        print(f"   Recall: {model_info['performance']['recall']}")
    use_new_ml = True
else:
    print("⚠️  NEW ML model not available. Start it with:")
    print("   cd 'ML Model/ML Model' && python -m uvicorn fastapi_server:app --reload --port 8000")
    use_new_ml = False
    
    # Fallback to old systems
    try:
        from career_engine_ml import HybridCareerEngine, MLCareerEngine
        ml_engine = HybridCareerEngine()
        use_ml = True
        print("✅ Using old ML-based career recommendations (fallback)")
    except Exception as e:
        print(f"⚠️  Old ML engine not available: {e}")
        from career_engine import CareerEngine, process_career_recommendation
        use_ml = False
        print("⚠️  Falling back to rule-based system")

# Import comprehensive roadmaps for all 24 ML careers
from comprehensive_roadmaps import get_roadmap
from course_api import get_course_recommendations

app = Flask(__name__, static_folder='.', static_url_path='')
app.secret_key = 'your-secret-key-here-change-in-production'  # Required for sessions

# Define the model path - use relative path for better portability
model_path = 'career_recommendation_model.pkl'

# Load model with error handling
try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    print(f"Model loaded successfully from {model_path}")
except Exception as e:
    print(f"Error loading model: {str(e)}")
    model = None

# Column names for the features
columns = [f'Q{i}' for i in range(1, 21)]  # Q1 to Q20

# Career explanations
career_descriptions = {
    "Software Developer": "Software developers design, build, and maintain computer programs. Your assessment shows strong analytical thinking and problem-solving abilities, which are essential in this field.",
    
    "Data Scientist": "Data scientists analyze and interpret complex data to help organizations make better decisions. Your results indicate strong analytical skills and comfort with data analysis.",
    
    "Marketing Manager": "Marketing managers develop strategies to promote products and services. Your profile shows creativity combined with business acumen, which suits this role well.",
    
    "Healthcare Professional": "Healthcare professionals provide medical care and support to patients. Your assessment indicates strong empathy and helping orientation, which are fundamental in this field.",
    
    "Teacher/Educator": "Teachers inspire and educate students of various ages. Your results suggest strong communication skills and a desire to help others grow and develop.",
    
    "Financial Analyst": "Financial analysts assess financial data and make recommendations for investments and business decisions. Your assessment shows strong numerical reasoning and analytical thinking.",
    
    "Project Manager": "Project managers coordinate resources and people to complete projects. Your profile indicates good organizational and leadership skills necessary for this role.",
    
    "Human Resources Manager": "HR managers oversee employee relations, recruitment, and organizational development. Your assessment shows strong interpersonal skills and interest in human behavior.",
    
    "Entrepreneur": "Entrepreneurs start and manage their own businesses. Your results suggest creativity, risk tolerance, and independent thinking that entrepreneurs typically possess.",
    
    "Graphic Designer": "Graphic designers create visual concepts for various media. Your assessment indicates strong creative thinking and artistic abilities."
}

# Default explanation for careers not in our dictionary
default_explanation = "This career aligns with your personality traits and preferences based on the psychometric assessment patterns of professionals in this field."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pages/<path:filename>')
def serve_pages(filename):
    """Serve static HTML pages from pages folder"""
    from flask import send_from_directory
    return send_from_directory('pages', filename)

@app.route('/quiz')
def quiz():
    questions = [
        "I enjoy solving complex logical and mathematical problems",
        "I can work on the same task consistently for long periods",
        "I prefer structured, step-by-step approaches to problem-solving",
        "I get frustrated when requirements keep changing",
        "I enjoy creating visual designs and user interfaces",
        "I like experimenting with new ideas and approaches",
        "I prefer seeing quick results from my work",
        "I'm comfortable with ambiguous or unclear requirements",
        "I can maintain focus on long-term goals without immediate rewards",
        "I enjoy learning new technologies independently",
        "I prefer detailed documentation and clear instructions",
        "I'm comfortable making decisions with incomplete information",
        "I can stay motivated even when progress is slow",
        "I enjoy teaching or explaining concepts to others",
        "I prefer working on one project deeply rather than multiple projects",
        "I'm comfortable with trial-and-error learning",
        "I enjoy optimizing and improving existing systems",
        "I prefer creative freedom over following strict guidelines",
        "I'm patient with debugging and troubleshooting",
        "I enjoy competitive environments and challenges"
    ]
    return render_template('quiz.html', questions=questions)

@app.route('/career-guide')
def career_guide():
    """New career guide intake form"""
    return render_template('career_guide.html')

@app.route('/process-career-guide', methods=['POST'])
def process_career_guide():
    """Process career guide form and generate recommendations using NEW ML model"""
    try:
        # Prepare quiz data for ML API
        quiz_data = {}
        
        # Numeric questions (Q1-Q10) - 1-5 scale
        for i in range(1, 11):
            quiz_data[f'Q{i}'] = float(request.form.get(f'Q{i}', 3))
        
        # Categorical questions (Q11-Q22)
        quiz_data['Q11_work_env'] = request.form.get('work_env', 'Flexible')
        quiz_data['Q12_team_size'] = request.form.get('team_size', 'Small (2-5)')
        quiz_data['Q13_risk'] = request.form.get('risk', 'Medium')
        quiz_data['Q14_pace'] = request.form.get('pace', 'Moderate')
        quiz_data['Q15_values'] = request.form.get('values', 'Making impact')
        quiz_data['Q16_prefers'] = request.form.get('prefers', 'Mix of all')
        quiz_data['Q17_balance'] = request.form.get('balance', 'Very')
        quiz_data['Q18_education'] = request.form.get('education', 'Bachelors')
        quiz_data['Q19_subjects'] = request.form.get('subjects', 'Mixed')
        quiz_data['Q20_coding'] = request.form.get('coding', 'Basic')
        quiz_data['Q21_indoor'] = request.form.get('indoor', 'Mostly indoor')
        quiz_data['Q22_age'] = request.form.get('age', '23-27')
        
        # Text questions (Q23-Q26) - for SBERT embeddings
        quiz_data['Q23_problem_text'] = request.form.get('problem_text', '')
        quiz_data['Q24_dream_text'] = request.form.get('dream_text', '')
        quiz_data['Q25_skill_text'] = request.form.get('skill_text', '')
        quiz_data['Q26_achievements'] = request.form.get('achievements_text', '')  # NEW: Achievements field
        
        # Get constraints
        constraints = {
            "time_per_week": int(request.form.get('time_per_week', 10)),
            "academic_year": request.form.get('academic_year', 'year2'),
            "financial": request.form.get('financial', 'medium'),
            "internet": request.form.get('internet', 'yes') == 'yes',
            "device": request.form.get('device', 'laptop'),
            "interest": request.form.get('interest', 'internship'),
            "experience_level": request.form.get('experience_level', 'beginner')
        }
        
        # Use NEW ML model if available
        if use_new_ml and ml_client.is_available:
            ml_result = ml_client.predict_career(quiz_data)
            
            if ml_result and ml_result.get('success'):
                top_careers = ml_result['top5_careers']
                
                # Format for template
                result = {
                    'primary_path': {
                        'name': top_careers[0]['career'],
                        'key': top_careers[0]['career'].lower().replace(' ', '_').replace('/', '_'),
                        'score': top_careers[0]['ml_confidence'],
                        'rationale': f"ML Confidence: {top_careers[0]['ml_confidence']}%. "
                                   f"Readiness Score: {top_careers[0]['readiness_score']}%. "
                                   f"Based on {top_careers[0]['data_source']}.",
                        'outcomes': top_careers[0]['skills_required'][:3],
                        'method': 'XGBoost + SBERT (all-MiniLM-L6-v2)',
                        'skills_gap': top_careers[0]['skills_gap'],
                        'skills_you_have': top_careers[0]['skills_you_have'],
                        'skills_required': top_careers[0]['skills_required'],
                        'readiness_score': top_careers[0]['readiness_score'],
                        'model_metrics': top_careers[0]['model_metrics']
                    },
                    'secondary_path': {
                        'name': top_careers[1]['career'],
                        'key': top_careers[1]['career'].lower().replace(' ', '_').replace('/', '_'),
                        'score': top_careers[1]['ml_confidence'],
                        'rationale': f"ML Confidence: {top_careers[1]['ml_confidence']}%. "
                                   f"Readiness Score: {top_careers[1]['readiness_score']}%. "
                                   f"Alternative career path with strong alignment.",
                        'outcomes': top_careers[1]['skills_required'][:3],
                        'method': 'XGBoost + SBERT (all-MiniLM-L6-v2)',
                        'skills_gap': top_careers[1]['skills_gap'],
                        'skills_you_have': top_careers[1]['skills_you_have'],
                        'skills_required': top_careers[1]['skills_required'],
                        'readiness_score': top_careers[1]['readiness_score'],
                        'model_metrics': top_careers[1]['model_metrics']
                    },
                    'all_predictions': top_careers,
                    'model_info': ml_result['model_info'],
                    'constraints': constraints,
                    'using_new_ml': True
                }
                
                # Store in session for roadmap generation
                session['career_recommendation'] = result
                session['constraints'] = constraints
                
                return render_template('career_recommendation.html', result=result)
            else:
                # ML API failed, fall back
                print("⚠️  ML API prediction failed, using fallback")
        
        # Fallback to old system if new ML not available or failed
        print("⚠️  Using fallback system")
        try:
            if 'ml_engine' in globals() and ml_engine:
                # Use old ML system
                result = ml_engine.recommend_career(quiz_data, constraints)
            else:
                # Use rule-based system
                from career_engine import process_career_recommendation
                result = process_career_recommendation(quiz_data, constraints)
        except Exception as fallback_error:
            print(f"❌ Fallback system also failed: {fallback_error}")
            # Last resort: create a basic result
            result = {
                'primary_path': {
                    'name': 'Software Engineer',
                    'key': 'software_engineer',
                    'score': 75,
                    'rationale': 'Based on your responses, software engineering is a good fit.',
                    'outcomes': ['Programming', 'Problem Solving', 'System Design']
                },
                'secondary_path': {
                    'name': 'Data Scientist',
                    'key': 'data_scientist',
                    'score': 70,
                    'rationale': 'Alternative path with strong analytical focus.',
                    'outcomes': ['Data Analysis', 'Statistics', 'Machine Learning']
                },
                'constraints': constraints
            }
        
        result['using_new_ml'] = False
        session['career_recommendation'] = result
        session['constraints'] = constraints
        
        return render_template('career_recommendation.html', result=result)
        
    except Exception as e:
        print(f"❌ Error in process_career_guide: {e}")
        import traceback
        traceback.print_exc()
        
        # Return to career guide with error message instead of rendering non-existent error.html
        return render_template('career_guide.html', error=f"Error generating recommendations: {str(e)}. Please try again."), 500

@app.route('/commit-path', methods=['POST'])
def commit_path():
    """Handle 90-day commitment"""
    try:
        chosen_path = request.form.get('chosen_path', 'primary')
        result = session.get('career_recommendation')
        
        print(f"=== COMMIT PATH DEBUG ===")
        print(f"Chosen path type: {chosen_path}")
        print(f"Session has recommendation: {result is not None}")
        
        if not result:
            print("ERROR: No career recommendation in session")
            return redirect(url_for('career_guide'))
        
        # Get the chosen path details
        if chosen_path == 'primary':
            path = result['primary_path']
        else:
            path = result['secondary_path']
        
        print(f"Path selected: {path['name']}")
        print(f"Path key: {path['key']}")
        
        # Store commitment
        session['active_career_path'] = {
            "path_key": path['key'],
            "path_name": path['name'],
            "committed_date": result.get('timestamp', datetime.now().isoformat()),
            "current_week": 1,
            "current_phase": "Foundation"
        }
        session.modified = True
        
        print(f"Commitment stored successfully")
        
        # Note: The roadmap will be initialized in Firebase when the user views it
        # The roadmap_visual.html JavaScript will call initializeRoadmap() automatically
        print(f"Redirecting to roadmap view - Firebase initialization will happen on page load")
        
        # Redirect to roadmap view
        return redirect(url_for('view_roadmap', path_key=path['key']))
        
    except Exception as e:
        error_message = f"Error committing to path: {str(e)}"
        print(f"ERROR: {error_message}")
        import traceback
        traceback.print_exc()
        
        # Return error page instead of redirecting
        return render_template('career_recommendation.html', 
                             error=f"Failed to generate roadmap: {str(e)}. Please try again.")

@app.route('/my-roadmap')
def my_roadmap():
    """View current roadmap (redirect to specific path)"""
    commitment = session.get('active_career_path')
    
    if not commitment:
        return redirect(url_for('career_guide'))
    
    path_key = commitment.get('path_key')
    return redirect(url_for('view_roadmap', path_key=path_key))

@app.route('/my-roadmaps')
def my_roadmaps():
    """View all user's roadmaps"""
    return render_template('my_roadmaps.html')

@app.route('/system-info')
def system_info():
    """Check which recommendation system is active"""
    if use_new_ml:
        model_info = ml_predictor.get_model_info()
        return jsonify({
            "status": "NEW ML Model Active",
            "engine": "XGBoost Classifier + SBERT",
            "text_model": "all-MiniLM-L6-v2 (384-dim embeddings)",
            "accuracy": f"{model_info['performance']['accuracy']*100:.2f}%",
            "precision": f"{model_info['performance']['precision']*100:.2f}%",
            "f1_score": f"{model_info['performance']['f1_score']*100:.2f}%",
            "careers_supported": len(model_info['careers']),
            "data_sources": model_info['data_sources'],
            "model_loaded": True,
            "message": "✅ Using NEW ML model (XGBoost + SBERT all-MiniLM-L6-v2)"
        })
    elif use_ml:
        try:
            from career_engine_ml import MLCareerEngine
            ml = MLCareerEngine()
            if ml.model_loaded:
                return jsonify({
                    "status": "Old ML-Powered (Fallback)",
                    "engine": "Random Forest Classifier",
                    "accuracy": "85%+",
                    "model_loaded": True,
                    "message": "✅ Using old ML-based career recommendations"
                })
            else:
                return jsonify({
                    "status": "Rule-Based (Fallback)",
                    "engine": "Hybrid System",
                    "model_loaded": False,
                    "message": "⚠️ ML model not trained. Run 'python train_ml_model.py' to enable ML."
                })
        except:
            return jsonify({
                "status": "Rule-Based",
                "engine": "Algorithm-based",
                "message": "⚠️ ML engine not available"
            })
    else:
        return jsonify({
            "status": "Rule-Based",
            "engine": "Algorithm-based",
            "message": "Using traditional rule-based system"
        })

@app.route('/view-roadmap/<path_key>')
def view_roadmap(path_key):
    """View specific roadmap by path key"""
    # Get roadmap data (node-based format)
    roadmap_data = get_roadmap(path_key)
    
    if not roadmap_data or not roadmap_data.get('nodes'):
        return redirect(url_for('career_guide'))
    
    # Create or get commitment for this path
    commitment = session.get('active_career_path', {})
    if not commitment or commitment.get('path_key') != path_key:
        commitment = {
            'path_key': path_key,
            'path_name': roadmap_data.get('name', 'Career Path'),
            'current_week': 1,
            'current_phase': 'Foundation'
        }
        session['active_career_path'] = commitment
        session.modified = True
    
    # Render the visual roadmap template
    return render_template('roadmap_visual.html', 
                         roadmap_data=roadmap_data,
                         commitment=commitment)

@app.route('/api/courses/<path_key>')
def get_courses(path_key):
    """API endpoint to get course recommendations for a career path"""
    try:
        recommendations = get_course_recommendations(path_key)
        return jsonify(recommendations)
    except Exception as e:
        return jsonify({
            'error': str(e),
            'message': 'Failed to fetch course recommendations'
        }), 500

@app.route('/api/courses/search/<query>')
def search_courses(query):
    """API endpoint to search courses by query"""
    try:
        from course_api import CourseRecommendationService
        service = CourseRecommendationService()
        
        # Search YouTube
        youtube_url = f"{service.youtube_base_url}/search"
        params = {
            'part': 'snippet',
            'q': query,
            'type': 'video,playlist',
            'maxResults': 10,
            'key': service.youtube_api_key,
            'order': 'relevance'
        }
        
        if service.youtube_api_key != 'YOUR_YOUTUBE_API_KEY':
            response = requests.get(youtube_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            courses = []
            for item in data.get('items', []):
                item_type = item['id'].get('kind', '').split('#')[-1]
                item_id = item['id'].get('videoId') or item['id'].get('playlistId')
                
                course = {
                    'id': item_id,
                    'title': item['snippet']['title'],
                    'description': item['snippet']['description'][:200] + '...',
                    'thumbnail': item['snippet']['thumbnails']['medium']['url'],
                    'channel': item['snippet']['channelTitle'],
                    'url': f"https://www.youtube.com/{'watch?v=' if item_type == 'video' else 'playlist?list='}{item_id}",
                    'type': item_type,
                    'platform': 'YouTube',
                    'kind': item['id']['kind']
                }
                courses.append(course)
            
            return jsonify({
                'query': query,
                'courses': courses,
                'total': len(courses)
            })
        else:
            return jsonify({
                'error': 'YouTube API key not configured',
                'message': 'Please configure YOUTUBE_API_KEY environment variable'
            }), 500
            
    except Exception as e:
        return jsonify({
            'error': str(e),
            'message': 'Failed to search courses'
        }), 500

@app.route('/api/ml/predict', methods=['POST'])
def api_ml_predict():
    """API endpoint to test new ML model predictions"""
    try:
        if not use_new_ml:
            return jsonify({
                'error': 'New ML model not available',
                'message': 'Model artifacts not found or failed to load'
            }), 503
        
        # Get quiz answers from request
        data = request.get_json()
        
        # Predict
        result = ml_predictor.predict(data, top_n=5)
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'message': 'Failed to generate predictions'
        }), 500

@app.route('/api/ml/info')
def api_ml_info():
    """Get detailed ML model information"""
    try:
        if not use_new_ml:
            return jsonify({
                'error': 'New ML model not available'
            }), 503
        
        model_info = ml_predictor.get_model_info()
        return jsonify(model_info)
        
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

@app.route('/api/ml/careers')
def api_ml_careers():
    """Get list of all supported careers"""
    try:
        if not use_new_ml:
            return jsonify({
                'error': 'New ML model not available'
            }), 503
        
        careers = ml_predictor.get_all_careers()
        return jsonify({
            'total': len(careers),
            'careers': careers
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if model is None:
            return render_template('result.html', error="Model could not be loaded. Please contact the administrator.")
        
        career_label_to_name = {
             "Career_0": "Data Scientist",
    "Career_1": "Psychologist",
    "Career_2": "Software Engineer",
    "Career_3": "Artist",
    "Career_4": "Doctor",
    "Career_5": "Teacher",
    "Career_6": "Business Analyst",
    "Career_7": "Engineer",
    "Career_8": "Biologist",
    "Career_9": "Entrepreneur",
    "Career_10": "Journalist",
    "Career_11": "Marketing Manager",
    "Career_12": "Nurse",
    "Career_13": "Accountant",
    "Career_14": "UX Designer",
    "Career_15": "Financial Analyst",
    "Career_16": "Architect",
    "Career_17": "Social Worker",
    "Career_18": "IT Support Specialist",
    "Career_19": "Chef",
    "Career_20": "Human Resources Manager",
    "Career_21": "Research Scientist",
    "Career_22": "Lawyer",
    "Career_23": "Electrician",
    "Career_24": "Graphic Designer",
    "Career_25": "Product Manager",
    "Career_26": "Civil Engineer",
    "Career_27": "Veterinarian",
    "Career_28": "Consultant",
    "Career_29": "Pharmacist",
    "Career_30": "Event Planner",
    "Career_31": "Mechanical Engineer",
    "Career_32": "Environmental Scientist",
    "Career_33": "Real Estate Agent",
    "Career_34": "Physical Therapist",
    "Career_35": "Supply Chain Manager",
    "Career_36": "Web Developer",
    "Career_37": "Customer Service Rep",
    "Career_38": "Project Manager",
    "Career_39": "College Professor",
    "Career_40": "Dental Hygienist",
    "Career_41": "Pilot",
    "Career_42": "Cybersecurity Analyst",
    "Career_43": "Fashion Designer",
    "Career_44": "Speech Therapist",
    "Career_45": "Investment Banker",
    "Career_46": "Photographer",
    "Career_47": "Clinical Psychologist",
    "Career_48": "Game Developer",
    "Career_49": "Urban Planner",
    "Career_50": "Flight Attendant",
    "Career_51": "Robotics Engineer",
    "Career_52": "Environmental Lawyer",
    "Career_53": "Interior Designer",
    "Career_54": "Music Teacher",
    "Career_55": "Data Analyst",
    "Career_56": "Dentist",
    "Career_57": "Fitness Trainer",
    "Career_58": "Aerospace Engineer",
    "Career_59": "Content Creator",
    "Career_60": "Occupational Therapist",
    "Career_61": "Financial Planner",
    "Career_62": "App Developer",
    "Career_63": "Marriage Counselor",
    "Career_64": "Geologist",
    "Career_65": "Chef de Cuisine",
    "Career_66": "Public Relations Specialist",
    "Career_67": "Neurologist",
    "Career_68": "Architect (Software)",
    "Career_69": "Social Media Manager",
    "Career_70": "Physicist",
    "Career_71": "Landscape Designer",
    "Career_72": "Emergency Medical Technician",
    "Career_73": "Air Traffic Controller",
    "Career_74": "Historian",
    "Career_75": "Hotel Manager",
    "Career_76": "Nuclear Engineer",
    "Career_77": "Marine Biologist",
    "Career_78": "Art Director",
    "Career_79": "Dental Assistant",
    "Career_80": "Mechanical Technician",
    "Career_81": "Special Education Teacher",
    "Career_82": "Technical Writer",
    "Career_83": "Pharmaceutical Sales",
    "Career_84": "Forensic Scientist",
    "Career_85": "Athletic Trainer",
    "Career_86": "Database Administrator",
    "Career_87": "Interior Decorator",
    "Career_88": "Nurse Practitioner",
    "Career_89": "Financial Controller",
    "Career_90": "UI Developer",
    "Career_91": "School Counselor",
    "Career_92": "Geophysicist",
    "Career_93": "Executive Chef",
    "Career_94": "Digital Marketing Specialist",
    "Career_95": "Cardiologist",
    "Career_96": "DevOps Engineer",
    "Career_97": "Public Speaker",
    "Career_98": "Quantum Physicist",
    "Career_99": "Floral Designer",
    "Career_100": "Speech-Language Pathologist",
    "Career_101": "Investment Analyst",
    "Career_102": "3D Artist",
    "Career_103": "Clinical Nurse Specialist",
    "Career_104": "Tax Accountant",
    "Career_105": "UX Researcher",
    "Career_106": "Marriage Therapist",
    "Career_107": "Astronomer",
    "Career_108": "Restaurant Manager",
    "Career_109": "SEO Specialist",
    "Career_110": "Surgical Technologist",
    "Career_111": "Machine Learning Engineer",
    "Career_112": "Event Host",
    "Career_113": "Meteorologist",
    "Career_114": "Fashion Merchandiser",
    "Career_115": "Physical Education Teacher",
    "Career_116": "Systems Administrator",
    "Career_117": "Interior Architect",
    "Career_118": "Genetic Counselor",
    "Career_119": "Actuary",
    "Career_120": "Video Game Artist",
    "Career_121": "Speech Coach",
    "Career_122": "Astronaut"
        }
        
        # Get user responses
        responses = [int(request.form[f'Q{i+1}']) for i in range(20)]
        df = pd.DataFrame([responses], columns=columns)
        
        # Get prediction probabilities
        proba = model.predict_proba(df)[0]
        classes = model.classes_

        # Get top 5 recommendations
        top_n = sorted(zip(classes, proba), key=lambda x: x[1], reverse=True)[:5]
        
        # Format recommendations with explanations
        recommendations = []
        for job, score in top_n:
            # Get explanation for the career (use default if not found)
            explanation = career_descriptions.get(job, default_explanation)
            
            # Add strength-based insights based on user responses
            high_scores = []
            for i, response in enumerate(responses):
                if response >= 4:  # User scored high (4 or 5)
                    high_scores.append(i)
            
            # Map question indices to skills
            skills_map = {
                0: "analytical thinking",
                1: "helping others",
                2: "working with hands",
                3: "creativity",
                4: "business acumen",
                5: "technical understanding",
                6: "interest in natural systems",
                7: "data analysis",
                8: "organizational skills",
                9: "independent work",
                10: "teamwork",
                11: "leadership",
                12: "attention to detail",
                13: "adaptability",
                14: "understanding human behavior",
                15: "communication",
                16: "social contribution",
                17: "challenge-seeking",
                18: "work-life balance",
                19: "decision-making"
            }
            
            # Pick up to 3 relevant high-scoring skills
            relevant_skills = [skills_map[i] for i in high_scores[:3]]
            if relevant_skills:
                explanation += "<br><br>Your strengths in " + ", ".join(relevant_skills) + " are particularly valuable in this career path."

            
            career_name = career_label_to_name.get(job, job)
            
            recommendations.append({
                'career': career_name,
                'confidence': round(score * 1000, 2),
                'explanation': explanation
            })

        return render_template('result.html', recommendations=recommendations)

    except Exception as e:
        error_message = f"Error processing prediction: {str(e)}"
        print(error_message)
        return render_template('result.html', error=error_message)

if __name__ == '__main__':
    app.run(debug=True)