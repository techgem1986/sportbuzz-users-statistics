def handler(event, context):
    uid = event.uid
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": "Welcome " + uid + "to AWS Lambda using Python"
    }
