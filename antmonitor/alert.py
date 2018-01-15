from .utils import GetConfig
import click


def SendAlert(Message):
    context = click.get_current_context()
    cli_notificaiton = context.meta['alert']
    try:
        config_notification = GetConfig('alert,notify')
    except KeyError as e:
        raise click.UsageError('Configuration Failure\nCould not find Alert Notification setting')

    try:
        config_aws_key = GetConfig('credentials,aws,key')
        config_aws_secret = GetConfig('credentials,aws,secret')
    except KeyError as e:
        raise click.UsageError('Configuration Failure\nCould not find AWS Credential setting')

    import boto3
    sns = boto3.client(
        'sns',
        aws_access_key_id=config_aws_key,
        aws_secret_access_key=config_aws_secret
    )

    if config_notification or cli_notificaiton:
        try:
            topic = GetConfig('alert,snstopic')
        except KeyError as e:
            raise click.UsageError('Failure Sending Alert\nCould not find SNS Topic')

        try:
            response = sns.publish(
                TopicArn=topic,
                Message=Message,
                Subject='Antmonitor Alert'
            )
            return response['MessageId']
        except Exception as e:
            raise click.UsageError('There was a problem sending an alert')
