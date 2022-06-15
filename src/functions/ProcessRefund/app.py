from __future__ import print_function
import json
import urllib
import boto3
import datetime

print('Loading function...')

def process_refund(message, context):

    #Input Example
    #{'TransactionType': 'REFUND'}

    #1. Log input message
    print("Recieved message from Step Functions")
    print(message)

    #2 Construct Response object
    response = {}
    response['TransactionType'] = message['TransactionType']
    response['Timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    response['Message'] = 'Hello from lambda land inside the ProcessRefund function'

    return response