import json

def handler(event, context):
  try:
    body = json.loads(event.get("body", "{}"))
    workout_id = body.get("id")
    user_id = body.get("userId")
    workout_title = body.get("workoutTitle")
    date_and_time = body.get("dateAndTime")
    exercises = body.get("exercises", [])

    if not workout_id or not user_id or not workout_title or not date_and_time or not exercises:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Missing required fields"})
        }

    # In production, you'd store in DynamoDB here.

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Workout created", "workout": body})
    }
  except Exception as e:
    return {
      "statusCode": 500,
      "body": json.dumps({"error": str(e)})
    }