import json

import boto3
from boto3.dynamodb.conditions import Key

from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return str(obj)
    return json.JSONEncoder.default(self, obj)

# products = [
#         {
#             "id": 1,
#             "name": "iPhone"
#         },
#          {
#             "id": 2,
#             "name": "Moto"
#         },
#          {
#             "id": 3,
#             "name": "Samsung Galaxy"
#         },
#     ]

def lambda_handler(event, context):
    # TODO implement
    print("event", event)
    
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Products')
    
    
    args = {}
    response = table.scan(**args)
    
    products = response.get('Items', [])

    return {
        'statusCode': 200,
        'body': json.dumps(products, cls=DecimalEncoder)
    }
