import json

def handler(event, context):
  try:
    body = json.loads(event.get("body", "{}"))
    user_id = body.get("userId")
    date = body.get("date")
    exercises = body.get("exercises", [])

    if not user_id or not date or not exercises:
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