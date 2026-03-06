"""
ML-Based Career Recommendation System Trainer
Trains a Random Forest model on psychometric assessment data
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import json

def load_and_prepare_data(csv_path='psychometric_dataset.csv'):
    """Load and prepare the dataset"""
    print("Loading dataset...")
    df = pd.read_csv(csv_path)
    
    # Separate features and target
    X = df.iloc[:, :-1]  # All columns except last (Q1-Q30)
    y = df.iloc[:, -1]   # Last column (Job_Role)
    
    print(f"Dataset shape: {df.shape}")
    print(f"Features: {X.shape[1]} questions")
    print(f"Samples: {len(df)}")
    print(f"Career paths: {y.nunique()}")
    print(f"\nCareer distribution:")
    career_counts = y.value_counts()
    print(career_counts)
    
    # Show mapping to 12 main paths
    print(f"\n📊 Dataset has {y.nunique()} career types")
    print(f"💡 These are the 12 career paths:")
    print(f"   1. Software Engineer (Backend/Systems)")
    print(f"   2. Frontend Developer")
    print(f"   3. Full Stack Developer")
    print(f"   4. Data Scientist/Analyst")
    print(f"   5. UI/UX Designer")
    print(f"   6. DevOps/Cloud Engineer")
    print(f"   7. Mobile App Developer")
    print(f"   8. AI/ML Engineer")
    print(f"   9. Cybersecurity Specialist")
    print(f"   10. Product Manager")
    print(f"   11. Digital Marketing Specialist")
    print(f"   12. Business Analyst")
    
    return X, y

def train_model(X, y):
    """Train Random Forest model"""
    print("\n" + "="*50)
    print("TRAINING ML MODEL")
    print("="*50)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"\nTraining set: {len(X_train)} samples")
    print(f"Test set: {len(X_test)} samples")
    
    # Train Random Forest
    print("\nTraining Random Forest Classifier...")
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=20,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    )
    
    model.fit(X_train, y_train)
    
    # Predictions
    y_pred = model.predict(X_test)
    
    # Accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\n✅ Test Accuracy: {accuracy*100:.2f}%")
    
    # Cross-validation
    cv_scores = cross_val_score(model, X, y, cv=5)
    print(f"✅ Cross-Validation Accuracy: {cv_scores.mean()*100:.2f}% (+/- {cv_scores.std()*100:.2f}%)")
    
    # Feature importance
    feature_importance = pd.DataFrame({
        'feature': [f'Q{i+1}' for i in range(X.shape[1])],
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print("\n📊 Top 5 Most Important Questions:")
    print(feature_importance.head())
    
    # Classification report
    print("\n📋 Classification Report:")
    print(classification_report(y_test, y_pred))
    
    return model, accuracy, feature_importance, y_test, y_pred

def save_model(model, accuracy, feature_importance):
    """Save trained model and metadata"""
    print("\n" + "="*50)
    print("SAVING MODEL")
    print("="*50)
    
    # Save model
    model_path = 'career_ml_model.pkl'
    joblib.dump(model, model_path)
    print(f"✅ Model saved: {model_path}")
    
    # Save metadata
    metadata = {
        'accuracy': float(accuracy),
        'model_type': 'RandomForestClassifier',
        'n_estimators': 100,
        'features': 30,
        'career_paths': list(model.classes_),
        'feature_importance': feature_importance.to_dict('records')
    }
    
    with open('model_metadata.json', 'w') as f:
        json.dump(metadata, f, indent=2)
    print("✅ Metadata saved: model_metadata.json")
    
    return model_path

def test_prediction(model):
    """Test model with sample input"""
    print("\n" + "="*50)
    print("TESTING MODEL")
    print("="*50)
    
    # Sample input (30 questions, values 1-5)
    sample_input = np.array([[4, 5, 3, 5, 5, 2, 3, 3, 3, 5, 4, 3, 5, 2, 4, 2, 4, 5, 1, 4, 3, 4, 5, 3, 2, 4, 3, 5, 4, 3]])
    
    prediction = model.predict(sample_input)
    probabilities = model.predict_proba(sample_input)[0]
    
    print(f"\n📝 Sample Input: {sample_input[0]}")
    print(f"🎯 Predicted Career: {prediction[0]}")
    print(f"\n📊 Confidence Scores:")
    
    # Get top 3 predictions
    top_3_idx = np.argsort(probabilities)[-3:][::-1]
    for idx in top_3_idx:
        career = model.classes_[idx]
        confidence = probabilities[idx] * 100
        print(f"   {career}: {confidence:.2f}%")

def main():
    """Main training pipeline"""
    print("\n" + "="*60)
    print("🚀 ML-BASED CAREER RECOMMENDATION SYSTEM TRAINER")
    print("="*60)
    
    # Load data
    X, y = load_and_prepare_data()
    
    # Train model
    model, accuracy, feature_importance, y_test, y_pred = train_model(X, y)
    
    # Save model
    model_path = save_model(model, accuracy, feature_importance)
    
    # Test prediction
    test_prediction(model)
    
    print("\n" + "="*60)
    print("✅ TRAINING COMPLETE!")
    print("="*60)
    print(f"\n📦 Model file: {model_path}")
    print(f"📊 Accuracy: {accuracy*100:.2f}%")
    print(f"\n💡 Next steps:")
    print("   1. Use 'career_ml_model.pkl' in your Flask app")
    print("   2. Update career_engine.py to use ML predictions")
    print("   3. Deploy and test with real users")
    print("\n")

if __name__ == "__main__":
    main()
