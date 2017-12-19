import boto3
sns = boto3.client('sns')


def SendAlert(Message):
    print('alert')
