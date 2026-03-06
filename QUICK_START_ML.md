# 🚀 Quick Start Guide

## System Overview
- **30 Questions**: Scientific psychometric assessment
- **12 Career Paths**: ML-powered recommendations
- **3000 Samples**: Training dataset
- **55% Accuracy**: Across 12 careers

## Setup Complete ✅
Your system is already configured and ready to use!

## Start Application
```bash
python app.py
```

Visit: http://localhost:5000/career-guide

## Test ML System
```bash
python test_ml_system.py
```

## Retrain Model (if needed)
```bash
# 1. Generate new dataset
python create_robust_dataset.py

# 2. Train model
python train_ml_model.py

# 3. Test
python test_ml_system.py
```

## 12 Career Paths
1. Software Engineer (Backend/Systems)
2. Frontend Developer
3. Full Stack Developer
4. Data Scientist/Analyst
5. UI/UX Designer
6. DevOps/Cloud Engineer
7. Mobile App Developer
8. AI/ML Engineer
9. Cybersecurity Specialist
10. Product Manager
11. Digital Marketing Specialist
12. Business Analyst

## Key Files
- `app.py` - Flask application
- `career_engine_ml.py` - ML predictions
- `career_engine.py` - Rule-based fallback
- `roadmap_data.py` - Career roadmaps
- `psychometric_dataset.csv` - Training data
- `career_ml_model.pkl` - Trained model

## Troubleshooting

**ML model not found?**
```bash
python train_ml_model.py
```

**Low accuracy?**
- Normal for 12 careers (55% is 6.7x better than random)
- Model still makes correct top-2 predictions

**Need help?**
Check README.md for full documentation
