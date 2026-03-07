"""
fastapi_server.py
Run: python -m uvicorn fastapi_server:app --reload --port 8000
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import pickle
import json
from sentence_transformers import SentenceTransformer

# ─────────────────────────────────────────
# LOAD
# ─────────────────────────────────────────
print("Loading model artifacts...")
model        = pickle.load(open("model_artifacts/career_model.pkl","rb"))
le_career    = pickle.load(open("model_artifacts/career_encoder.pkl","rb"))
scaler       = pickle.load(open("model_artifacts/scaler.pkl","rb"))
cat_encoders = pickle.load(open("model_artifacts/cat_encoders.pkl","rb"))
metrics      = json.load(open("model_artifacts/metrics.json"))
per_career   = json.load(open("model_artifacts/metrics_per_career.json"))
skills_ref   = json.load(open("model_artifacts/career_skills_reference.json"))
feat_info    = json.load(open("model_artifacts/feature_info.json"))
sbert        = SentenceTransformer('all-MiniLM-L6-v2')
print("✅ All artifacts loaded!")

app = FastAPI(title="CareerIQ API", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# ─────────────────────────────────────────
# SCHEMA
# ─────────────────────────────────────────
class QuizAnswers(BaseModel):
    Q1_realistic:      float = 3.0
    Q2_investigative:  float = 3.0
    Q3_artistic:       float = 3.0
    Q4_social:         float = 3.0
    Q5_enterprising:   float = 3.0
    Q6_conventional:   float = 3.0
    Q7_math:           float = 3.0
    Q8_communication:  float = 3.0
    Q9_technical:      float = 3.0
    Q10_design:        float = 3.0
    Q11_work_env:      str = "Flexible"
    Q12_team_size:     str = "Small (2-5)"
    Q13_risk:          str = "Medium"
    Q14_pace:          str = "Moderate"
    Q15_values:        str = "Making impact"
    Q16_prefers:       str = "Mix of all"
    Q17_balance:       str = "Very"
    Q18_education:     str = "Bachelors"
    Q19_subjects:      str = "Mixed"
    Q20_coding:        str = "Basic"
    Q21_indoor:        str = "Mostly indoor"
    Q22_age:           str = "23-27"
    Q23_problem_text:  str = ""
    Q24_dream_text:    str = ""
    Q25_skill_text:    str = ""
    Q26_achievements:  str = ""  # NEW: Achievements field


# ─────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────
def build_features(a: QuizAnswers):
    numeric = [
        a.Q1_realistic, a.Q2_investigative, a.Q3_artistic,
        a.Q4_social, a.Q5_enterprising, a.Q6_conventional,
        a.Q7_math, a.Q8_communication, a.Q9_technical, a.Q10_design
    ]
    cat_vals = {
        'Q11_work_env':a.Q11_work_env,'Q12_team_size':a.Q12_team_size,
        'Q13_risk':a.Q13_risk,'Q14_pace':a.Q14_pace,
        'Q15_values':a.Q15_values,'Q16_prefers':a.Q16_prefers,
        'Q17_balance':a.Q17_balance,'Q18_education':a.Q18_education,
        'Q19_subjects':a.Q19_subjects,'Q20_coding':a.Q20_coding,
        'Q21_indoor':a.Q21_indoor,'Q22_age':a.Q22_age,
    }
    encoded = []
    for col, val in cat_vals.items():
        le = cat_encoders.get(col)
        try:    encoded.append(int(le.transform([str(val)])[0]))
        except: encoded.append(0)

    text = f"Problem I love: {a.Q23_problem_text} | My dream: {a.Q24_dream_text} | My best skill: {a.Q25_skill_text} | My achievements: {a.Q26_achievements}"
    emb  = sbert.encode([text])[0]
    return np.hstack([np.array(numeric + encoded), emb]).reshape(1,-1)


def skill_gap(career, a: QuizAnswers):
    required = skills_ref.get(career, [])
    have = []
    if a.Q9_technical >= 3:    have += ["Python","Programming","Technical Skills","Coding","SQL"]
    if a.Q7_math >= 3:         have += ["Mathematics","Statistics","Analytical Skills"]
    if a.Q8_communication >= 3:have += ["Communication","Writing","Presentation"]
    if a.Q10_design >= 3:      have += ["Design","Visual Communication","Creativity"]
    if a.Q20_coding in ["Intermediate","Advanced","Expert"]: have += ["Git","Data Analysis","Algorithms"]
    have_lower = [h.lower() for h in have]
    matched = [s for s in required if any(h in s.lower() or s.lower() in h for h in have_lower)]
    gap     = [s for s in required if s not in matched]
    return {
        "skills_required": required,
        "skills_you_have": matched,
        "skills_gap":      gap,
        "readiness_score": round(len(matched)/len(required)*100) if required else 50,
    }


# ─────────────────────────────────────────
# ENDPOINTS
# ─────────────────────────────────────────
@app.post("/predict")
async def predict(answers: QuizAnswers):
    try:
        feat    = scaler.transform(build_features(answers))
        proba   = model.predict_proba(feat)[0]
        top5    = proba.argsort()[-5:][::-1]
        results = []
        for rank, idx in enumerate(top5, 1):
            career = le_career.classes_[idx]
            conf   = round(float(proba[idx])*100, 1)
            cm     = per_career.get(career, {})
            sg     = skill_gap(career, answers)
            results.append({
                "rank":            rank,
                "career":          career,
                "ml_confidence":   conf,
                "model_metrics":   {"precision":cm.get("precision",0),"recall":cm.get("recall",0),"f1_score":cm.get("f1_score",0)},
                "skills_required": sg["skills_required"],
                "skills_you_have": sg["skills_you_have"],
                "skills_gap":      sg["skills_gap"],
                "readiness_score": sg["readiness_score"],
                "data_source":     "O*NET v28.2 (US Dept of Labor) + BLS OEWS 2024",
            })
        return {
            "success":      True,
            "top5_careers": results,
            "model_info":   {
                "algorithm":        "XGBoost Classifier",
                "text_processing":  "SBERT all-MiniLM-L6-v2 (384-dim embeddings)",
                "training_data":    "O*NET v28.2 + BLS OEWS 2024",
                "overall_f1":       metrics["overall_metrics"]["f1_score"],
                "overall_precision":metrics["overall_metrics"]["precision"],
                "overall_recall":   metrics["overall_metrics"]["recall"],
                "feature_dims":     feat_info["total_features"],
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/metrics")
def get_metrics():
    return metrics

@app.get("/metrics/per-career")
def get_per_career():
    return {"description":"Per-career precision/recall/F1 from test set","metrics":per_career}

@app.get("/model-info")
def get_model_info():
    return {
        "model":   "XGBoost Classifier",
        "problem": "Multi-class Classification (24 careers)",
        "data_sources":[
            {"name":"O*NET v28.2","org":"US Dept of Labor","url":"https://www.onetcenter.org"},
            {"name":"BLS OEWS 2024","org":"Bureau of Labor Statistics","url":"https://www.bls.gov/oes/"},
        ],
        "input_processing":{
            "mcq":   "22 features via LabelEncoder + StandardScaler",
            "text":  "SBERT all-MiniLM-L6-v2 → 384-dim semantic embeddings",
            "total": feat_info["total_features"],
        },
        "performance":        metrics["overall_metrics"],
        "cross_validation":   metrics["cross_validation"],
    }

@app.get("/careers")
def list_careers():
    return {"total":len(le_career.classes_),"careers":list(le_career.classes_)}

@app.get("/")
def root():
    return {
        "service":"CareerIQ API","status":"running",
        "endpoints":[
            "POST /predict            → Top 5 career predictions",
            "GET  /metrics            → Overall precision/recall/F1",
            "GET  /metrics/per-career → Per-career breakdown",
            "GET  /model-info         → Full model transparency",
            "GET  /careers            → All 24 supported careers",
            "GET  /docs               → Interactive API docs",
        ]
    }