from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .app.schemas import PredictionRequest, PredictionResponse
from .app.utils import get_prediction


app = FastAPI(docs_url="/")
app.title = "Movie Revenue Prediction"
app.version = "0.0.1"


@app.post("/v1/prediction", tags=["prediction"], status_code=200)
def make_model_prediction(request: PredictionRequest):
    prediction = get_prediction(request)
    prediction_dict = {"worldwide_gross": prediction}
    return JSONResponse(content=prediction_dict, status_code=200)


# {
#   "opening_gross": 77025481.0 ,
#   "screens": 3452.0,
#   "production_budget": 425000000,
#   "title_year": 2009,
#   "aspect_ratio": 1.78,
#   "duration": 178.0,
#   "cast_total_facebook_likes": 4834,
#   "budget": 237000000.0,
#   "imdb_score": 7.9
# }


# {
#   "production_budget": 425000000,
#   "title_year": 2009,
#   "aspect_ratio": 1.78,
#   "duration": 178.0,
#   "cast_total_facebook_likes": 4834,
#   "budget": 237000000.0,
#   "imdb_score": 7.9,
#   "opening_gross": 77025481.0 ,
#   "screens": 3452.0,
# }
