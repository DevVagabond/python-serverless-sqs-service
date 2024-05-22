# consumer handler to handle sqs message
import os

from util.util import format_response
import boto3


def consumer(event, context):
    sqsMessage = event['Records'][0]['body']
    print('Consumer handler called', sqsMessage)
    print('Event: {}'.format(event))
    return format_response({"message": "Message received from SQS queue"})
