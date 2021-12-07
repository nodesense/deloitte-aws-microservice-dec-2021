import json

def lambda_handler(event, context):
    # TODO implement
    print("Event", event)
    
    processed = []
    
    for message in event["Records"]:
        body = message["body"]
        print("body ", body)
        inv = json.loads(body)
        
        print("processing stock ", inv["stock_code"], "qty ", inv["qty"])
        processed.append(inv)
    
    return {
        'statusCode': 200,
        'body': json.dumps(processed)
    }
