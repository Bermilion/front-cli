# -*- coding: utf-8 -*-

import os
import click
import subprocess
from common import getConfig, controlDir, listPresets

env = os.environ
directory = env['HOME'] + '/.front-cli'
presetDir = env['HOME'] + '/.front-cli/presets'
conf = getConfig()

def checking(name):
    projectsDir = conf['root-dir']
    if projectsDir:
        return controlDir(projectsDir, name)
    else:
        return controlDir(os.getcwd(), name)

@click.command()
# @click.option('--clone', '-c', default=False, help='Клонирование репозитория')
# @click.option('--update', '-u', is_flag=True, help='Выкачивает последние изменения в присетах.')
# @click.option('--delete', '-d', default=False, help='Удаляет пресет.')
@click.option('--list', '-l', is_flag=True)
@click.argument('name', nargs=-1)
def init(name, list):
    """Разворачивает новый проект из пресета"""

#     click.secho('\nОпции команды init', fg='green', bold=True)
#     click.echo("""  --clone, -c       Добавляет пресет в список пресетов.\n
#   --update, -u      Выкачивает последние изменения в присетах.\n
#   --delete, -d      Удаляет пресет.\n
#   --list, -l           Выводит список локально доступных пресетов.
# """)

    if name != ():
        if checking(name[0]):
            listPresets(True)
    elif name == () and list:
        click.echo('active option')
    else:
        name = raw_input('Название проекта: ')
        if checking(name):
            listPresets(True)
