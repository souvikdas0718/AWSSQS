import boto3
import random

# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'https://sqs.us-east-1.amazonaws.com/983957969826/halifaxDineOrders'

food_List = ['pizza', 'pasta','sandwich','noodles','ice cream','wrap','brownie','pie','smoothie','coffee','tea','rice']
quantity = list(range(1,11))
# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    MessageAttributes={
        'item': {
            'DataType': 'String',
            'StringValue': str(random.choice(food_List))
        },
        'quantity': {
            'DataType': 'Number',
            'StringValue': str(random.choice(quantity))
        }
    },
    MessageBody=(
        'This is my first order'
    )
)

print(response['MessageId'])