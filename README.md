# Titanic Survival Predictor API

A machine learning API that predicts whether a Titanic passenger would have survived, based on ticket fare, age, sex, and passenger class.

## Built With
- XGBoost
- FastAPI
- Python

## How to Run

1. Install dependencies:
```bash
pip install fastapi uvicorn xgboost
```

2. Start the server:
```bash
uvicorn main:app --reload
```

3. Visit `http://127.0.0.1:8000/docs` to test the API.

## Example Request

```json
{
  "fare": 100,
  "age": 25,
  "sex": 1,
  "pclass": 1
}
```

Returns `{"survived": 1}` or `{"survived": 0}`.
