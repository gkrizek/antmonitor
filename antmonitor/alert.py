from utils import GetConfig
import boto3
import click
sns = boto3.client('sns')


def SendAlert(Message):
    context = click.get_current_context()
    cli_notificaiton = context.meta['alert']
    try:
        config_notification = GetConfig('alert,notify')
    except KeyError as e:
        raise click.UsageError('Configuration Failure\nCould not find Alert Notification setting')

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
        except:
            raise click.UsageError('There was a problem sending an alert')
