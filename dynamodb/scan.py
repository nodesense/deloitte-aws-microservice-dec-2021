from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Products')

args = {}
response = table.scan(**args)

items = response.get('Items', [])

print (items)
