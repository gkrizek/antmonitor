import click
import os
import json
import re


def Validate():
    """
    Check if .antmonitor.cfg exists
    """
    if os.path.isfile(os.path.join(os.path.expanduser('~'),'.antmonitor.cfg')):
        try:
            json.load(open(os.path.join(os.path.expanduser('~'),'.antmonitor.cfg')))
        except ValueError as e:
            raise click.UsageError(str(e) + '\nPlease make sure your \'~/.antmonitor.cfg\' is valid JSON')
    else:
        raise click.UsageError('No such file: \'~/.antmonitor.cfg\'\nPlease make sure it exists and has proper permissions')

    """
    Check Values in Config
    """
    config = json.load(open(os.path.join(os.path.expanduser('~'),'.antmonitor.cfg')))

    # Miners
    try:
        config['miners']
    except KeyError as e:
        raise click.BadParameter('miners\n\nYou haven\'t specified any miners\nPlease add this section to your \'~/.antmonitor.cfg\'')

    try:
        config['miners']['antminers']
    except KeyError as e:
        raise click.BadParameter('antminers\n\nYou haven\'t specified any antminers\nPlease add this section to your \'~/.antmonitor.cfg\'')

    if len(config['miners']['antminers']) is 0:
        raise click.BadParameter('antminers\n\nYou haven\'t specified any antminers\nPlease add the IP or Hostnames to your \'~/.antmonitor.cfg\'')

    #Creds
    try:
        config['credentials']
    except KeyError as e:
        raise click.BadParameter('credentials\n\nYou haven\'t specified any credentials\nPlease add this section to your \'~/.antmonitor.cfg\'')

    try:
        config['credentials']['aws']
    except KeyError as e:
        raise click.BadParameter('aws\n\nYou haven\'t specified any aws credentials\nPlease add this section to your \'~/.antmonitor.cfg\'')

    try:
        config['credentials']['antminer']
    except KeyError as e:
        raise click.BadParameter('antminer\n\nYou haven\'t specified any antminer credentials\nPlease add this section to your \'~/.antmonitor.cfg\'')
