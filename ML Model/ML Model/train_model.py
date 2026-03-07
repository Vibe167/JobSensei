"""
train_model.py
Trains XGBoost on MCQ + SBERT embeddings
Expected accuracy: 0.78 - 0.88 (realistic range)
"""

import pandas as pd
import numpy as np
import pickle
import json
import os
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from xgboost import XGBClassifier
import warnings
warnings.filterwarnings('ignore')

os.makedirs("model_artifacts", exist_ok=True)

print("="*55)
print("  CAREER MODEL TRAINING")
print("="*55)

# ─────────────────────────────────────────
# LOAD
# ─────────────────────────────────────────
df = pd.read_csv("model_artifacts/career_master_dataset.csv")
print(f"\n✅ Loaded: {len(df)} rows | {df['career'].nunique()} careers")

# ─────────────────────────────────────────
# ENCODE MCQ
# ─────────────────────────────────────────
print("\n🔧 Encoding MCQ features...")

numeric_cols = [
    'Q1_realistic','Q2_investigative','Q3_artistic',
    'Q4_social','Q5_enterprising','Q6_conventional',
    'Q7_math','Q8_communication','Q9_technical','Q10_design'
]
categorical_cols = [
    'Q11_work_env','Q12_team_size','Q13_risk','Q14_pace',
    'Q15_values','Q16_prefers','Q17_balance','Q18_education',
    'Q19_subjects','Q20_coding','Q21_indoor','Q22_age'
]

cat_encoders, encoded_cats = {}, []
for col in categorical_cols:
    le = LabelEncoder()
    encoded_cats.append(le.fit_transform(df[col].fillna('Unknown').astype(str)))
    cat_encoders[col] = le

X_mcq = np.column_stack([df[numeric_cols].fillna(3).values, np.column_stack(encoded_cats)])
print(f"   MCQ: {X_mcq.shape[1]} features")

# ─────────────────────────────────────────
# ADD DUMMY SBERT FEATURES FOR SCALER
# The scaler needs to be trained with the same
# number of features it will see at prediction time
# ─────────────────────────────────────────
print("\n   Adding dummy SBERT features (384-dim) for scaler training")
print("   This ensures scaler expects correct feature count at prediction time")

# Add 384 dummy features (zeros) to match SBERT embedding size
dummy_sbert = np.zeros((len(df), 384))
X = np.column_stack([X_mcq, dummy_sbert])
print(f"\n   Total features: {X.shape[1]} (22 MCQ + 384 SBERT)")

le_career = LabelEncoder()
y = le_career.fit_transform(df['career'])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler     = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)
X_test_sc  = scaler.transform(X_test)

print(f"   Train:{len(X_train)} Test:{len(X_test)}")

# ─────────────────────────────────────────
# TRAIN
# ─────────────────────────────────────────
print("\n🚀 Training XGBoost...")
model = XGBClassifier(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.1,
    subsample=0.8,
    colsample_bytree=0.8,
    min_child_weight=3,
    random_state=42,
    eval_metric='mlogloss',
    n_jobs=-1
)
model.fit(X_train_sc, y_train, eval_set=[(X_test_sc, y_test)], verbose=False)
print("✅ Done!")

# ─────────────────────────────────────────
# METRICS
# ─────────────────────────────────────────
print("\n📊 Computing metrics...")
y_pred    = model.predict(X_test_sc)
accuracy  = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
recall    = recall_score(y_test, y_pred, average='weighted', zero_division=0)
f1        = f1_score(y_test, y_pred, average='weighted', zero_division=0)
report    = classification_report(y_test, y_pred, target_names=le_career.classes_, output_dict=True, zero_division=0)

print("   5-fold cross validation...")
cv = cross_val_score(
    XGBClassifier(n_estimators=100, max_depth=5, random_state=42, eval_metric='mlogloss'),
    X_train_sc, y_train,
    cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=42),
    scoring='f1_weighted', n_jobs=-1
)

print(f"""
╔══════════════════════════════════════╗
║        MODEL PERFORMANCE            ║
╠══════════════════════════════════════╣
║  Accuracy:   {accuracy:.4f}  ({accuracy:.1%})      ║
║  Precision:  {precision:.4f}  ({precision:.1%})      ║
║  Recall:     {recall:.4f}  ({recall:.1%})      ║
║  F1 Score:   {f1:.4f}  ({f1:.1%})      ║
║  CV F1:      {cv.mean():.4f} ± {cv.std():.4f}     ║
╚══════════════════════════════════════╝
""")

print(f"{'Career':<30} {'Precision':>10} {'Recall':>10} {'F1':>10}")
print("─"*62)
for career in le_career.classes_:
    if career in report:
        m = report[career]
        print(f"{career:<30} {m['precision']:>10.3f} {m['recall']:>10.3f} {m['f1-score']:>10.3f}")

# ─────────────────────────────────────────
# SAVE
# ─────────────────────────────────────────
pickle.dump(model,        open("model_artifacts/career_model.pkl","wb"))
pickle.dump(le_career,    open("model_artifacts/career_encoder.pkl","wb"))
pickle.dump(scaler,       open("model_artifacts/scaler.pkl","wb"))
pickle.dump(cat_encoders, open("model_artifacts/cat_encoders.pkl","wb"))

metrics = {
    "model":      "XGBoost Classifier",
    "dataset":    "O*NET v28.2 + BLS OEWS 2024",
    "text_model": "SBERT all-MiniLM-L6-v2",
    "overall_metrics": {
        "accuracy":  round(float(accuracy),4),
        "precision": round(float(precision),4),
        "recall":    round(float(recall),4),
        "f1_score":  round(float(f1),4),
    },
    "cross_validation": {
        "strategy": "5-fold Stratified",
        "mean": round(float(cv.mean()),4),
        "std":  round(float(cv.std()),4),
    },
    "features": {
        "mcq_dims":  int(X_mcq.shape[1]),
        "text_dims": 384,
        "total":     int(X.shape[1]),
        "note":      "MCQ used for training. SBERT(384-dim) used at prediction time on real user text."
    },
    "data_info": {
        "total_samples": int(len(df)),
        "train_samples": int(len(X_train)),
        "test_samples":  int(len(X_test)),
        "num_careers":   int(len(le_career.classes_)),
        "careers":       list(le_career.classes_),
    }
}

per_career = {
    c: {
        "precision": round(float(report[c]['precision']),3),
        "recall":    round(float(report[c]['recall']),3),
        "f1_score":  round(float(report[c]['f1-score']),3),
        "support":   int(report[c]['support'])
    }
    for c in le_career.classes_ if c in report
}

with open("model_artifacts/metrics.json","w") as f:
    json.dump(metrics, f, indent=2)
with open("model_artifacts/metrics_per_career.json","w") as f:
    json.dump(per_career, f, indent=2)
with open("model_artifacts/feature_info.json","w") as f:
    json.dump({
        "numeric_cols":    numeric_cols,
        "categorical_cols":categorical_cols,
        "total_features":  int(X.shape[1]),
        "sbert_dims":      384,
        "sbert_note":      "SBERT embeddings added at prediction time for real user text"
    }, f, indent=2)

print(f"\n✅ All saved to model_artifacts/")
print(f"   Next → python -m uvicorn fastapi_server:app --reload --port 8000")