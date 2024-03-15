from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)


# def test_null_prediction():
#     response = client.post(
#         "v1/prediction", 
#         json = {
#             "production_budget": 0,
#             "title_year": 0,
#             "aspect_ratio": 0,
#             "duration": 0,
#             "cast_total_facebook_likes": 0,
#             "budget": 0,
#             "imdb_score": 0,
#             "opening_gross": 0 ,
#             "screens": 0,
#         }
#     )
#     assert response.status_code == 200
#     assert response.json()["worldwide_gross"] == 0


def test_random_prediction():
    response = client.post(
        "v1/prediction", 
        json = {
            "production_budget": 425000000,
            "title_year": 2009,
            "aspect_ratio": 1.78,
            "duration": 178.0,
            "cast_total_facebook_likes": 4834,
            "budget": 237000000.0,
            "imdb_score": 7.9,
            "opening_gross": 77025481.0 ,
            "screens": 3452.0,
        }
    )
    assert response.status_code == 200
    assert response.json()["worldwide_gross"] != 0
    # assert response.json()["worldwide_gross"] == 2754233290.1244297



