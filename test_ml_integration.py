"""
Test ML Model Integration
Run this to verify the ML API is working correctly
"""

from ml_api_client import get_ml_client
import json

def test_ml_integration():
    print("="*60)
    print("  ML MODEL INTEGRATION TEST")
    print("="*60)
    
    # Get ML client
    client = get_ml_client()
    
    # Check availability
    print("\n1. Checking ML API availability...")
    if client.is_available:
        print("   ✅ ML API is running at http://localhost:8000")
    else:
        print("   ❌ ML API is NOT running")
        print("   Start it with: python start_ml_server.bat")
        return False
    
    # Get model info
    print("\n2. Getting model information...")
    model_info = client.get_model_info()
    if model_info:
        print(f"   ✅ Model: {model_info['model']}")
        print(f"   ✅ F1 Score: {model_info['performance']['f1_score']}")
        print(f"   ✅ Precision: {model_info['performance']['precision']}")
        print(f"   ✅ Recall: {model_info['performance']['recall']}")
    else:
        print("   ❌ Could not get model info")
        return False
    
    # Get supported careers
    print("\n3. Getting supported careers...")
    careers = client.get_supported_careers()
    if careers:
        print(f"   ✅ {len(careers)} careers supported:")
        for i, career in enumerate(careers[:5], 1):
            print(f"      {i}. {career}")
        if len(careers) > 5:
            print(f"      ... and {len(careers) - 5} more")
    else:
        print("   ❌ Could not get careers list")
        return False
    
    # Test prediction with sample data
    print("\n4. Testing prediction with sample data...")
    sample_quiz = {
        "Q1": 4.0,  # Realistic
        "Q2": 5.0,  # Investigative
        "Q3": 3.0,  # Artistic
        "Q4": 3.0,  # Social
        "Q5": 3.0,  # Enterprising
        "Q6": 4.0,  # Conventional
        "Q7": 5.0,  # Math
        "Q8": 4.0,  # Communication
        "Q9": 5.0,  # Technical
        "Q10": 3.0, # Design
        "Q11_work_env": "Flexible",
        "Q12_team_size": "Small (2-5)",
        "Q13_risk": "Medium",
        "Q14_pace": "Fast",
        "Q15_values": "Making impact",
        "Q16_prefers": "Problem solving",
        "Q17_balance": "Very",
        "Q18_education": "Bachelors",
        "Q19_subjects": "STEM",
        "Q20_coding": "Intermediate",
        "Q21_indoor": "Mostly indoor",
        "Q22_age": "23-27",
        "Q23_problem_text": "I love solving complex technical problems and building systems",
        "Q24_dream_text": "I want to be a software engineer working on impactful products",
        "Q25_skill_text": "Programming, problem solving, and learning new technologies"
    }
    
    result = client.predict_career(sample_quiz)
    
    if result and result.get('success'):
        print("   ✅ Prediction successful!")
        print(f"\n   Top 3 Career Predictions:")
        for i, career in enumerate(result['top5_careers'][:3], 1):
            print(f"\n   {i}. {career['career']}")
            print(f"      ML Confidence: {career['ml_confidence']}%")
            print(f"      Readiness Score: {career['readiness_score']}%")
            print(f"      Skills Required: {len(career['skills_required'])} skills")
            print(f"      Skills Gap: {len(career['skills_gap'])} skills to learn")
    else:
        print("   ❌ Prediction failed")
        return False
    
    print("\n" + "="*60)
    print("  ✅ ALL TESTS PASSED!")
    print("="*60)
    print("\nThe ML model is properly integrated and working.")
    print("You can now use the Career Guide in your app.")
    print("\nNext steps:")
    print("  1. Start Flask app: python app.py")
    print("  2. Visit: http://localhost:5000/career-guide")
    print("  3. Fill out the form and get ML-powered recommendations!")
    
    return True

if __name__ == "__main__":
    test_ml_integration()
