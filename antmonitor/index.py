import click

@click.group()
@click.option('--alert', '-a', is_flag=True, help="Send an alert if threshold is passed")
@click.option('--cron', '-c', is_flag=True, help="Only log if a threshold is passed")
@click.option('--quiet', '-q', is_flag=True, help="Don't log anything")
def main(alert, cron, quiet):
    """
    Antmonitor - Monitor your Antminer devices
    """
    click.echo('Alert is: ' + str(alert))

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

if __name__ == '__main__':
    main()
