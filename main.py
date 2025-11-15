import sqlite3

from config import settings
from data import SQLRepository
from fastapi import FastAPI
from model import GarchModel
from pydantic import BaseModel


# ---------------------------
# Request/Response Schemas
# ---------------------------

# Task 8.4.14, `FitIn` class
class FitIn(BaseModel):
    ticker: str
    use_new_data: bool
    n_observations: int
    p: int
    q: int


# Task 8.4.14, `FitOut` class
class FitOut(FitIn):
    success: bool
    message: str


# Task 8.4.18, `PredictIn` class
class PredictIn(BaseModel):
    ticker: str
    n_days: int


# Task 8.4.18, `PredictOut` class
class PredictOut(PredictIn):
    forecast: dict
    success: bool        # fixed to bool instead of str
    message: str


# ---------------------------
# Helper Functions
# ---------------------------

# Task 8.4.15
def build_model(ticker, use_new_data):
    # Create DB connection
    connection = sqlite3.connect(settings.db_name, check_same_thread=False)

    # Create `SQLRepository`
    repo = SQLRepository(connection=connection)

    # Create model
    model = GarchModel(ticker=ticker, use_new_data=use_new_data, repo=repo)

    # Return model
    return model


# ---------------------------
# FastAPI App
# ---------------------------

app = FastAPI()


# Task 8.4.11
@app.get("/hello", status_code=200)
def hello():
    """Return dictionary with greeting message."""
    return {"message": "Hello World!"}


# Task 8.4.16, `"/fit"` path
@app.post("/fit", status_code=200, response_model=FitOut)
def fit_model(request: FitIn):
    """Fit model, return confirmation message."""

    response = request.dict()

    try:
        # Build model
        model = build_model(ticker=request.ticker, use_new_data=request.use_new_data)

        # Wrangle data
        model.wrangle_data(n_observations=request.n_observations)

        # Fit model
        model.fit(p=request.p, q=request.q)

        # Save model
        filename = model.dump()

        response["success"] = True
        response["message"] = f"Trained and Saved '{filename}'."

    except Exception as e:
        response["success"] = False
        response["message"] = str(e)

    return response


# Task 8.4.19, `"/predict"` path
@app.post("/predict", status_code=200, response_model=PredictOut)
def get_prediction(request: PredictIn):
    """Load model and generate volatility prediction."""

    response = request.dict()

    try:
        # Build model (don't fetch new data, use stored model)
        model = build_model(ticker=request.ticker, use_new_data=False)

        # Load stored model
        model.load()

        # Generate prediction
        prediction = model.predict_volatility(horizon=request.n_days)

        response["success"] = True
        response["forecast"] = prediction
        response["message"] = ""

    except Exception as e:
        response["success"] = False
        response["forecast"] = {}
        response["message"] = str(e)

    return response
