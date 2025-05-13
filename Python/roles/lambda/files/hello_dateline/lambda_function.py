import json, datetime, os

def lambda_handler(event, context):
    now = datetime.datetime.utcnow().isoformat() + "Z"
    return {
        "statusCode": 200,
        "body": json.dumps({"time_utc": now})
    }
