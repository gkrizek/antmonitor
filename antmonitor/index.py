#!/usr/bin/env python

from utils import Validate, CreateConfig
import click

@click.group()
@click.option('--alert', '-a', is_flag=True, help="Send an alert if threshold is passed")
@click.option('--cron', '-c', is_flag=True, help="Only log if a threshold is passed")
@click.option('--quiet', '-q', is_flag=True, help="Don't log anything")
def main(alert, cron, quiet):
    """
    Antmonitor - Monitor your Antminer devices
    """
    context = click.get_current_context()
    context.meta['alert'] = alert
    context.meta['cron'] = cron
    context.meta['quiet'] = quiet
    Validate()

@main.command('temp', short_help="Check the temperature is above given temp")
def temp():
    click.echo('temp')

@main.command('memory', short_help="Check if free memory is below certain percentage")
def memory():
    click.echo('memory')

@main.command('pool', short_help="Check if Active Pool is what you expect it to be")
def pool():
    click.echo('pool')

@main.command('hashes', short_help="Check if number of GH/s is below certain number")
def hashes():
    click.echo('hashes')

@main.command('asic', short_help="Checks the ASIC status if any `o` are `x`")
def asic():
    click.echo('asic')

@main.command('all', short_help="Run all checks")
def all():
    click.echo('all')

@main.command('config', short_help="Creates a ~/.antmonitor.cfg file")
def config():
    click.echo(click.style('Warning: This will overwrite your existing ~/.antmonitor.cfg file', fg="yellow"))
    resume = click.confirm(click.style('Do you want to continue?\n', fg="yellow"), abort=True)
    miners = click.prompt('What are your miner IP Addresses? (comma seperated)', type=str)
    aws_key = click.prompt('What is your AWS Access Key? (type "none" if you wish not to specify)', type=str)
    aws_secret = click.prompt('What is your AWS Secret Key? (type "none" if you wish not to specify)', type=str)
    antminer_username = click.prompt('What is your Antminer username?', type=str)
    antminer_password = click.prompt('What is your Antminer password?', type=str)
    notify = click.confirm('Do you want to send alerts?')
    sns_topic = click.prompt('What is your AWS SNS Topic ARN? (type "none" if you wish not to specify)', type=str)
    temp = click.prompt('What is your max temperature threshold?', type=int, default=90)
    memory = click.prompt('What is your minimum free memory threshold?', type=int, default=10)
    pool = click.prompt('What is the URL for your expected active pool?', type=str)
    hashes = click.prompt('What is your minimum acceptable GH/s threshold?', type=int)

    creation = CreateConfig(
        Miners=miners,
        Key=aws_key,
        Secret=aws_secret,
        Username=antminer_username,
        Password=antminer_password,
        Notify=notify,
        SNS=sns_topic,
        Temp=temp,
        Mem=memory,
        Pool=pool,
        Hashes=hashes
    )
    click.echo(creation)

if __name__ == '__main__':
    main()
