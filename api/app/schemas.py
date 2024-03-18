from pydantic import BaseModel


class PredictionRequest(BaseModel):
    production_budget: int
    title_year: int
    aspect_ratio: float
    duration: float
    cast_total_facebook_likes: int
    budget: float
    imdb_score: float
    opening_gross: float
    screens: float

    class Config:
        """Example data schema."""

        schema_extra = {
            "example": {
                "production_budget": 425000000,
                "title_year": 2009,
                "aspect_ratio": 1.78,
                "duration": 178.0,
                "cast_total_facebook_likes": 4834,
                "budget": 237000000.0,
                "imdb_score": 7.9,
                "opening_gross": 77025481.0,
                "screens": 3452.0,
            }
        }


class PredictionResponse(BaseModel):
    worldwide_gross: float
