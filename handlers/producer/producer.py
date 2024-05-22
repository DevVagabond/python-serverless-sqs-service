import os

from util.util import format_response
import boto3


def producer(event, context):
    print('Producer handler called')
    print('Event: {}'.format(event))
    headers = event.get('headers')
    body = event.get('body')
    api_key = headers.get('x-api-key') if headers else None
    print('Headers: {}'.format(headers))
    if api_key != os.environ['API_KEY']:
        return format_response({"message": "Unauthorized"})
    sqs = boto3.client('sqs')

    sqs.send_message(
        QueueUrl=os.environ['SQS_URL'],
        MessageBody=body
    )
    return format_response({"message": "Message sent to SQS queue"})
