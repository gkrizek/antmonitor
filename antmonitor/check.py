from .alert import SendAlert
import click
import re
from .request import GetContent
import sys
from .utils import GetConfig


def TempCheck(Miner):
    content = GetContent(Miner, "minerStatus")

    try:
        config_temp = GetConfig('threshold,temp')
    except KeyError as e:
        config_temp = 90

    context = click.get_current_context()
    cli_cron = context.meta['cron']
    cli_quiet = context.meta['quiet']

    if temp > config_temp:
        if cli_quiet:
            sys.exit(1)
        else:
            alert = "Temperate too high for " + Miner + ". Received " + str(temp) + "."
            # SendAlert(alert)
            return alert
    else:
        if cli_cron or cli_quiet:
            return
        else:
            return "Temperature is OK for " + Miner + ". Received " + str(temp) + "."


def MemoryCheck(Miner):
    """
    Get Memory Value
    """

    try:
        config_memory = GetConfig('threshold,memory')
    except KeyError as e:
        memory = 10

    context = click.get_current_context()
    cli_cron = context.meta['cron']
    cli_quiet = context.meta['quiet']

    if memory > config_memory:
        if cli_quiet:
            sys.exit(1)
        else:
            alert = "Free Memory is too low for " + Miner + ". Received " + str(memory) + "%."
            # SendAlert(alert)
            return alert
    else:
        if cli_cron or cli_quiet:
            return
        else:
            return "Free Memory is OK for " + Miner + ". Received " + str(memory) + "."


def PoolCheck(Miner):
    """
    Get Pool Value
    """
    try:
        config_pool = GetConfig('threshold,pool')
    except KeyError as e:
        config_pool = True

    context = click.get_current_context()
    cli_cron = context.meta['cron']
    cli_quiet = context.meta['quiet']

    if config_pool:
        if pool is not config_pool:
            if cli_quiet:
                sys.exit(1)
            else:
                alert = "Pool is Dead on " + Miner + ". Received " + str(pool) + "."
                # SendAlert(alert)
                return alert
        else:
            if cli_cron or cli_quiet:
                return
            else:
                return "All pools are Active on " + Miner + "."


def HashCheck(Miner):
    """
    Get Hash Value
    """
    hashes = "1300"
    try:
        config_hashes = GetConfig('threshold,hashes')
    except KeyError as e:
        raise click.UsageError('Configuration Failure\nCould not find hashes threshold')

    context = click.get_current_context()
    cli_cron = context.meta['cron']
    cli_quiet = context.meta['quiet']

    if hashes < config_hashes:
        if cli_quiet:
            sys.exit(1)
        else:
            alert = "GH/s is low for " + Miner + ". Received " + str(hashes) + "."
            # SendAlert(alert)
            return alert
    else:
        if cli_cron or cli_quiet:
            return
        else:
            return "GH/s is OK for " + Miner + ". Received " + str(hashes) + "."


def FanCheck(Miner):
    """
    Get Fan Value
    """
    rpm = "1300"
    try:
        config_fan = GetConfig('threshold,fan')
    except KeyError as e:
        config_fan = 2000

    context = click.get_current_context()
    cli_cron = context.meta['cron']
    cli_quiet = context.meta['quiet']

    if rpm < config_fan:
        if cli_quiet:
            sys.exit(1)
        else:
            alert = "Fan speed is low for " + Miner + ". Received " + str(rpm) + "."
            # SendAlert(alert)
            return alert
    else:
        if cli_cron or cli_quiet:
            return
        else:
            return "Fan speed is OK for " + Miner + ". Received " + str(rpm) + "."


def AsicCheck(Miner):
    """
    Get ASIC Value
    """
    asic = "1300"

    context = click.get_current_context()
    cli_cron = context.meta['cron']
    cli_quiet = context.meta['quiet']

    if "x" in asic:
        if cli_quiet:
            sys.exit(1)
        else:
            alert = "Hashboard issue for " + Miner + ". Received " + str(asic) + "."
            # SendAlert(alert)
            return alert
    else:
        if cli_cron or cli_quiet:
            return
        else:
            return "Hashboards are OK for " + Miner + ". Received " + str(asic) + "."


def AllCheck(Miner):
    temp = TempCheck(Miner)
    print(temp)
    memory = MemoryCheck(Miner)
    print(memory)
    pool = PoolCheck(Miner)
    print(pool)
    hashes = HashCheck(Miner)
    print(hashes)
    fan = FanCheck(Miner)
    print(fan)
    asic = AsicCheck(Miner)
    print(asic)
    return "---"
