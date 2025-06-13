import json
from backend.handlers import create_workout

def test_create_workout_success():
    event = {
        "body": json.dumps({
            "id": "123",
            "userId": "123",
            "workoutTitle": "Push Day",
            "dateAndTime": "2025-06-08",
            "exercises": [
                {"name": "Bench Press", "sets": [{"reps": 10, "weight": 100}]}
            ]
        })
    }

    response = create_workout.handler(event, None)
    assert response["statusCode"] == 200
    assert "Workout created" in response["body"]
