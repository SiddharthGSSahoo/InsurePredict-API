from fastapi import FastAPI, HTTPException
from ModelClasses import InsuranceClaimInput
from fastapi.responses import JSONResponse
import joblib
import os

# Dynamically find the model file in the same directory as this script
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
MODEL_PATH=os.path.join(BASE_DIR,"final_insurance_model.pkl")

app=FastAPI()
try:
    model=joblib.load(MODEL_PATH)
except Exception as e:
    model=None
    print(f"Error loading model at {MODEL_PATH}: {e}")

@app.get("/")
def hello():
    return {"message":"Welcome to the Insurance Claim Prediction API!"}

@app.post("/predict")
def predict_claim(input_data: InsuranceClaimInput):
    if model is None:
        raise HTTPException(status_code=500,detail="Model not loaded. Please check the server logs.")
    
    try:
        df=input_data.to_dataframe()
        
        # Make prediction
        prediction=model.predict(df)
        probability=model.predict_proba(df)
        
        result="Yes" if prediction[0]==1 else "No"
        confidence=float(probability[0][prediction[0]])
        
        return JSONResponse(status_code=200,content={"Prediction": result,"Confidence": round(confidence, 4),"Input_Received": input_data.model_dump()})
        
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Prediction Error: {str(e)}")

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)
