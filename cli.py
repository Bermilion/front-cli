# -*- coding: utf-8 -*-

import click
import commands.config as config

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass

cli.add_command(config.config)

if __name__ == '__main__':
    cli()