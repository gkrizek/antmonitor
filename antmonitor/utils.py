import click
import os
import json


def Validate():
    command = click.get_current_context().invoked_subcommand
    if command == "config":
        return

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
    except KeyError:
        raise click.BadParameter('miners\n\nYou haven\'t specified any miners\nPlease add this section to your \'~/.antmonitor.cfg\'')

    try:
        config['miners']['antminers']
    except KeyError:
        raise click.BadParameter('antminers\n\nYou haven\'t specified any antminers\nPlease add this section to your \'~/.antmonitor.cfg\'')

    if len(config['miners']['antminers']) is 0:
        raise click.BadParameter('antminers\n\nYou haven\'t specified any antminers\nPlease add the IP or Hostnames to your \'~/.antmonitor.cfg\'')

    #Creds
    try:
        config['credentials']
    except KeyError:
        raise click.BadParameter('credentials\n\nYou haven\'t specified any credentials\nPlease add this section to your \'~/.antmonitor.cfg\'')

    try:
        config['credentials']['aws']
    except KeyError:
        raise click.BadParameter('aws\n\nYou haven\'t specified any aws credentials\nPlease add this section to your \'~/.antmonitor.cfg\'')

    try:
        config['credentials']['antminer']
    except KeyError:
        raise click.BadParameter('antminer\n\nYou haven\'t specified any antminer credentials\nPlease add this section to your \'~/.antmonitor.cfg\'')

    try:
        config['credentials']['antminer']['username']
    except KeyError:
        raise click.BadParameter('username\n\nYou haven\'t specified a username for the antminer ui\nPlease add this section to your \'~/.antmonitor.cfg\'')

    try:
        config['credentials']['antminer']['password']
    except KeyError:
        raise click.BadParameter('password\n\nYou haven\'t specified a password for the antminer ui\nPlease add this section to your \'~/.antmonitor.cfg\'')

    #Alert
    try:
        config['alert']
    except KeyError:
        raise click.BadParameter('alert\n\nYou haven\'t specified any alert settings\nPlease add this section to your \'~/.antmonitor.cfg\'')

    try:
        config['alert']['notify']
        if config['alert']['notify'] in [ True, 'true' ]:
            try:
                config['alert']['snstopic']
            except KeyError:
                raise click.BadParameter('snstopic\n\nYou haven\'t specified a sns topic\nPlease add this section to your \'~/.antmonitor.cfg\'')
    except KeyError:
        raise click.BadParameter('notify\n\nYou haven\'t specified a notification setting\nPlease add this section to your \'~/.antmonitor.cfg\'')

    #Threshold
    try:
        config['threshold']
    except KeyError:
        raise click.BadParameter('threshold\n\nYou haven\'t specified any threshold settings\nPlease add this section to your \'~/.antmonitor.cfg\'')

    try:
        config['threshold']['temp']
        try:
            int(config['threshold']['temp'])
        except ValueError:
            raise click.BadParameter('temp\n\nThreshold of \'temp\' must be an integer\nPlease add this section to your \'~/.antmonitor.cfg\'')
    except KeyError:
        raise click.BadParameter('temp\n\nYou haven\'t specified any \'temp\' threshold settings\nPlease add this section to your \'~/.antmonitor.cfg\'')

    try:
        config['threshold']['memory']
        try:
            int(config['threshold']['memory'])
        except ValueError:
            raise click.BadParameter('memory\n\nThreshold of \'memory\' must be an integer\nPlease add this section to your \'~/.antmonitor.cfg\'')
    except KeyError:
        raise click.BadParameter('memory\n\nYou haven\'t specified any \'memory\' threshold settings\nPlease add this section to your \'~/.antmonitor.cfg\'')

    try:
        config['threshold']['pool']
    except KeyError:
        raise click.BadParameter('pool\n\nYou haven\'t specified any \'pool\' threshold settings\nPlease add this section to your \'~/.antmonitor.cfg\'')

    try:
        config['threshold']['hashes']
        try:
            int(config['threshold']['hashes'])
        except ValueError:
            raise click.BadParameter('hashes\n\nThreshold of \'hashes\' must be an integer\nPlease add this section to your \'~/.antmonitor.cfg\'')
    except KeyError:
        raise click.BadParameter('hashes\n\nYou haven\'t specified any \'hashes\' threshold settings\nPlease add this section to your \'~/.antmonitor.cfg\'')
    return

def CreateConfig(Miners, Key, Secret, Username, Password, Notify, SNS, Temp, Mem, Pool, Hashes):
    miners = Miners.split(',')
    if Notify:
        notify = "true"
    else:
        notify = "false"
    config = {
        "miners": {
            "antminers": miners
        },
        "credentials": {
          "aws": {
            "key": Key,
            "secret": Secret
          },
          "antminer": {
            "username": Username,
            "password": Password
          }
        },
        "alert": {
          "notify": notify,
          "snstopic": SNS
        },
        "threshold": {
          "temp": Temp,
          "memory": Mem,
          "pool": Pool,
          "hashes": Hashes
        }
    }
    try:
        config_path = os.path.join(os.path.expanduser('~'),'.antmonitor.cfg')
        config_file = open(config_path,'w')
        config_file.write(json.dumps(config, indent=True, sort_keys=True))
        return "~/.antmonitor.cfg was successfully updated"
    except Exception:
        return "There was a problem writing ~/.antmonitor.cfg"
