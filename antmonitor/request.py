import click
import requests
from .utils import GetConfig


def GetContent(Miner, Page):
    try:
        config_username = GetConfig('credentials,antminer,username')
        config_password = GetConfig('credentials,antminer,password')
    except KeyError as e:
        raise click.UsageError('Configuration Failure\nCould not find Antminer Credentials setting')

    response = requests.get("http://" + Miner + "/" + Page, auth=(config_username, config_password))
    return response.content
