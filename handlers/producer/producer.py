import os

from util.util import format_response


def producer(event, context):
    print('Producer handler called')
    print('Event: {}'.format(event))
    headers = event.get('headers')
    api_key = headers.get('x-api-key') if headers else None
    print('Headers: {}'.format(headers))
    if api_key != os.environ['API_KEY']:
        return format_response({"message": "Unauthorized"})
    return format_response({"message": "Hello from Producer!"})
