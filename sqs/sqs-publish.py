import boto3
import json
client = boto3.client('sqs')


message = {
 "id": "1242",
  "stock_code": "MANGO",
  "qty": 2,
  "type": "sold"
}


res = client.send_message(
    QueueUrl='https://sqs.us-east-2.amazonaws.com/xxxxxxxxxxxxxxxxx/gk_inventory_queue.fifo',
    MessageBody=json.dumps(message),
    MessageDeduplicationId=message["id"],
    MessageGroupId='inventory'
)

print("response", res)
