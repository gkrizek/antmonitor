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
            return alert
    else:
        if cli_cron or cli_quiet:
            return
        else:
            return "Temperature is ok. Received " + str(temp) + "."


def MemoryCheck():
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
            alert = "Free Memory is too low. Received " + str(temp) + "%."
            #SendAlert(alert)
            return alert
    else:
        if cli_cron or cli_quiet:
            return
        else:
            return "Free Memory is ok. Received " + str(temp) + "."


def PoolCheck():
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
            alert = "Active Pool is not the desired pool. Received " + str(temp) + "."
            #SendAlert(alert)
            return alert
    else:
        if cli_cron or cli_quiet:
            return
        else:
            return "Active Pool is ok. Received " + str(temp) + "."


def HashCheck():
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
            alert = "GH/s is low. Received " + str(hashes) + "."
            #SendAlert(alert)
            return alert
    else:
        if cli_cron or cli_quiet:
            return
        else:
            return "GH/s is ok. Received " + str(hashes) + "."


def AsicCheck():
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
            alert = "Hashboard issue. Received " + str(asic) + "."
            #SendAlert(alert)
            return alert
    else:
        if cli_cron or cli_quiet:
            return
        else:
            return "Hashboards are ok. Received " + str(asic) + "."


def AllCheck():
    temp = TempCheck()
    print(temp)
    memory = MemoryCheck()
    print(memory)
    pool = PoolCheck()
    print(pool)
    hashes = HashCheck()
    print(hashes)
    asic = AsicCheck()
    print(asic)
    return "\n---\nCompleted all checks"
