import json
from ..handlers import create_workout

def test_create_workout_success():
    event = {
        "body": json.dumps({
            "userId": "123",
            "date": "2025-06-08",
            "exercises": [
                {"name": "Bench Press", "sets": [{"reps": 10, "weight": 100}]}
            ]
        })
    }

    response = create_workout.handler(event, None)
    assert response["statusCode"] == 200
    assert "Workout created" in response["body"]
