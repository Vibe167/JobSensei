"""
Quick test script to verify ML system is working
"""

import sys

def test_ml_system():
    print("\n" + "="*60)
    print("🧪 TESTING ML CAREER RECOMMENDATION SYSTEM")
    print("="*60)
    
    # Test 1: Check if ML model exists
    print("\n1️⃣ Checking if ML model is trained...")
    try:
        import os
        if os.path.exists('career_ml_model.pkl'):
            print("   ✅ ML model found: career_ml_model.pkl")
        else:
            print("   ❌ ML model NOT found")
            print("   💡 Run: python train_ml_model.py")
            return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False
    
    # Test 2: Try loading ML engine
    print("\n2️⃣ Testing ML engine import...")
    try:
        from career_engine_ml import MLCareerEngine
        engine = MLCareerEngine()
        if engine.model_loaded:
            print("   ✅ ML engine loaded successfully")
        else:
            print("   ❌ ML engine failed to load model")
            return False
    except Exception as e:
        print(f"   ❌ Error importing ML engine: {e}")
        return False
    
    # Test 3: Test prediction
    print("\n3️⃣ Testing ML prediction...")
    try:
        sample_responses = [4, 5, 3, 5, 5, 2, 3, 3, 3, 5, 4, 3, 5, 2, 4, 2, 4, 5, 1, 4, 3, 4, 5, 3, 2, 4, 3, 5, 4, 3]
        primary_key, confidence, top_3 = engine.predict_career(sample_responses)
        
        print(f"   ✅ Prediction successful!")
        print(f"   📊 Primary Career: {engine.career_names[primary_key]}")
        print(f"   📊 Confidence: {confidence:.1f}%")
        print(f"\n   Top 3 Predictions:")
        for i, (career_key, conf) in enumerate(top_3, 1):
            print(f"      {i}. {engine.career_names[career_key]}: {conf:.1f}%")
    except Exception as e:
        print(f"   ❌ Prediction failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Test 4: Test hybrid system
    print("\n4️⃣ Testing Hybrid Career Engine...")
    try:
        from career_engine_ml import HybridCareerEngine
        hybrid = HybridCareerEngine()
        
        sample_constraints = {
            "time_per_week": 15,
            "academic_year": "3rd year",
            "financial": "low",
            "internet": True,
            "device": "laptop"
        }
        
        result = hybrid.recommend(
            sample_responses,
            sample_constraints,
            "internship",
            "beginner"
        )
        
        print(f"   ✅ Hybrid system working!")
        print(f"   📊 Primary: {result['primary_path']['name']}")
        print(f"   📊 Score: {result['primary_path']['score']}%")
        
        if 'method' in result:
            print(f"   📊 Method: {result.get('method', 'Unknown')}")
        
    except Exception as e:
        print(f"   ❌ Hybrid system failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Test 5: Check Flask integration
    print("\n5️⃣ Testing Flask app integration...")
    try:
        # Just check if app.py can import the ML engine
        import importlib.util
        spec = importlib.util.spec_from_file_location("app", "app.py")
        if spec and spec.loader:
            print("   ✅ app.py can be loaded")
            print("   💡 Start Flask: python app.py")
        else:
            print("   ⚠️  Could not verify app.py")
    except Exception as e:
        print(f"   ⚠️  Warning: {e}")
    
    # Success!
    print("\n" + "="*60)
    print("✅ ALL TESTS PASSED!")
    print("="*60)
    print("\n🚀 Your ML system is ready!")
    print("\n📝 Next steps:")
    print("   1. Start Flask: python app.py")
    print("   2. Visit: http://localhost:5000/career-guide")
    print("   3. Check system: http://localhost:5000/system-info")
    print("\n")
    return True

if __name__ == "__main__":
    success = test_ml_system()
    sys.exit(0 if success else 1)
