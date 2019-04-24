# -*- coding: utf-8 -*-

import click
import commands.config as config
import commands.preset as preset
import commands.init as init

# CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

# @click.group(context_settings=CONTEXT_SETTINGS)
@click.group()
def cli():
    pass

cli.add_command(config.config)
cli.add_command(preset.preset)
cli.add_command(init.init)

if __name__ == '__main__':
    cli()