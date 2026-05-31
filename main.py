from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("titanic_model.pkl")

class Passenger(BaseModel):
    fare: float
    age: float
    sex: int
    pclass: int

@app.post("/predict")
def predict(passenger: Passenger):
    X = np.array([[passenger.fare, passenger.age, passenger.sex, passenger.pclass]])
    prediction = model.predict(X)[0]
    return {"survived": int(prediction)}
