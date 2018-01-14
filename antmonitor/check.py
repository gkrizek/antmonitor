from utils import GetConfig
from alert import SendAlert
import sys
import click


def TempCheck(Miner):
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
            alert = "Temperate too high for " + Miner + ". Received " + str(temp) + "."
            #SendAlert(alert)
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
    memory = 20
    try:
        config_memory = GetConfig('threshold,memory')
    except KeyError as e:
        raise click.UsageError('Configuration Failure\nCould not find memory threshold')

    context = click.get_current_context()
    cli_cron = context.meta['cron']
    cli_quiet = context.meta['quiet']

    if memory > config_memory:
        if cli_quiet:
            sys.exit(1)
        else:
            alert = "Free Memory is too low for " + Miner + ". Received " + str(temp) + "%."
            #SendAlert(alert)
            return alert
    else:
        if cli_cron or cli_quiet:
            return
        else:
            return "Free Memory is OK for " + Miner + ". Received " + str(temp) + "."


def PoolCheck(Miner):
    """
    Get Pool Value
    """
    pool = "abc123"
    try:
        config_pool = GetConfig('threshold,pool')
    except KeyError as e:
        raise click.UsageError('Configuration Failure\nCould not find pool threshold')

    context = click.get_current_context()
    cli_cron = context.meta['cron']
    cli_quiet = context.meta['quiet']

    if pool is not config_pool:
        if cli_quiet:
            sys.exit(1)
        else:
            alert = "Active Pool is not the desired pool for " + Miner + ". Received " + str(temp) + "."
            #SendAlert(alert)
            return alert
    else:
        if cli_cron or cli_quiet:
            return
        else:
            return "Active Pool is OK for " + Miner + ". Received " + str(temp) + "."


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
            #SendAlert(alert)
            return alert
    else:
        if cli_cron or cli_quiet:
            return
        else:
            return "GH/s is OK for " + Miner + ". Received " + str(hashes) + "."


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
            #SendAlert(alert)
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
    asic = AsicCheck(Miner)
    print(asic)
    return "\n---\nCompleted all checks"
