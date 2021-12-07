import boto3

client = boto3.client('sqs')
 
response = client.receive_message(
    QueueUrl='https://sqs.us-east-2.amazonaws.com/XXXXXXXXXXXXXXXXXXXX/gk_inventory_queue.fifo',
    MaxNumberOfMessages=5,
)

print("Response ", response)


# message = response['Messages'][0]
# # to delete message, we need to a handle [unique id in sqs]
# receipt_handle = message['ReceiptHandle']

# print("message", message)
# print("handle", receipt_handle)

for message in response['Messages']:
    body = message["Body"]
    # TODO: process the message content, after processing, delete the message
    receipt_handle = message['ReceiptHandle']

    print("message ", body)
    print("deleting message ", receipt_handle)

    client.delete_message(
        QueueUrl='https://sqs.us-east-2.amazonaws.com/XXXXXXXXXXXXXXXXXXXX/gk_inventory_queue.fifo',
        ReceiptHandle=receipt_handle
    )
