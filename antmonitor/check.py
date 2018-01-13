from utils import GetConfig
from alert import SendAlert
import sys
import click

def TempCheck():
    """
    Get Temp Value
    """
    temp = 90
    try:
        config_temp = GetConfig('threshold,temp')
    except KeyError as e:
        raise click.UsageError('Configuration Failure\nCould not find temperature threshold')

    context = click.get_current_context()
    cli_cron = context.meta['cron']
    cli_quiet = context.meta['quiet']

    if temp > config_temp:
        if cli_quiet:
            sys.exit(1)
        else:
            alert = "Temperate too high. Received " + str(temp) + "."
            #SendAlert(alert)
            print(alert)
            sys.exit(1)
    else:
        if cli_cron or cli_quiet:
            return
        else:
            return "Temperature OK. Received " + str(temp) + "."


def MemoryCheck():
    return

def PoolCheck():
    return

def HashCheck():
    return

def AsicCheck():
    return

def AllCheck():
    return
