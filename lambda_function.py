
def handler(event, context):
    print(event)
    print(context)
    uid = event['queryStringParameters']['uid']
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": "Welcome " + uid + "to AWS Lambda using Python"
    }
