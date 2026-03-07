#!/bin/bash

echo "========================================"
echo "Starting ML Model Server (FastAPI)"
echo "========================================"
echo ""
echo "This will start the XGBoost + SBERT model on port 8000"
echo "Make sure you have run the training first:"
echo "  1. cd 'ML Model/ML Model'"
echo "  2. python combine_datasets.py"
echo "  3. python train_model.py"
echo ""
echo "Starting server..."
echo ""

cd "ML Model/ML Model"
python -m uvicorn fastapi_server:app --reload --port 8000
