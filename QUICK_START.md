# 🚀 Quick Start Guide

## Get Your ML-Powered Career System Running in 5 Minutes

### Prerequisites
```bash
pip install fastapi uvicorn sentence-transformers xgboost scikit-learn pandas numpy flask
```

### Step 1: Train Model (First Time Only - 2 minutes)
```bash
cd "ML Model/ML Model"
python combine_datasets.py
python train_model.py
cd ../..
```

### Step 2: Start ML Server (Terminal 1)
```bash
# Windows
start_ml_server.bat

# Linux/Mac
chmod +x start_ml_server.sh
./start_ml_server.sh
```

Wait for: `Application startup complete`

### Step 3: Test Integration (Terminal 2)
```bash
python test_ml_integration.py
```

Wait for: `✅ ALL TESTS PASSED!`

### Step 4: Start Flask App (Terminal 2)
```bash
python app.py
```

### Step 5: Try It Out! 🎉
1. Open: http://localhost:5000/career-guide
2. Fill out the 30-question form
3. Get ML-powered career recommendations!

---

## What You Get

✅ **Top 5 Career Predictions** with confidence scores  
✅ **Skill Gap Analysis** - what you have vs what you need  
✅ **Readiness Scores** - how prepared you are  
✅ **Model Transparency** - see the AI's performance metrics  
✅ **Real Data** - based on O*NET v28.2 + BLS OEWS 2024  

---

## Troubleshooting

**ML Server won't start?**
```bash
# Check if port 8000 is free
netstat -ano | findstr :8000
```

**Model not found?**
```bash
# Make sure you ran Step 1
cd "ML Model/ML Model"
ls model_artifacts/
```

**Connection errors?**
- Ensure ML server shows "Application startup complete"
- Check http://localhost:8000/docs loads

---

## Architecture

```
Career Guide Form (30 questions)
    ↓
Flask App (Port 5000)
    ↓
ML API Client
    ↓
FastAPI Server (Port 8000)
    ↓
XGBoost + SBERT Model
    ↓
Career Predictions + Skill Gaps
```

---

## Need Help?

📖 Read: `ML_MODEL_INTEGRATION_GUIDE.md`  
🧪 Test: `python test_ml_integration.py`  
📊 API Docs: http://localhost:8000/docs  
✅ Complete Guide: `INTEGRATION_COMPLETE.md`

---

**That's it! You're ready to go! 🎉**
