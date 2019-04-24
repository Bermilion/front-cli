# -*- coding: utf-8 -*-

import os
import click
import subprocess

env = os.environ
directory = env['HOME'] + '/.front-cli'
presetDir = env['HOME'] + '/.front-cli/presets'
from common import listPresets

@click.command()
@click.option('--clone', '-c', default=False, help='Клонирование репозитория')
@click.option('--update', '-u', is_flag=True, help='Выкачивает последние изменения в присетах.')
@click.option('--delete', '-d', default=False, help='Удаляет пресет.')
@click.option('--list', '-l', is_flag=True, help='Выводит список локально доступных пресетов.')
def preset(clone, update, delete, list):
    """Служит для добаления репозитория как пресета"""

    click.secho('\nОпции команды preset', fg='green', bold=True)
    click.echo("""  --clone, -c       Добавляет пресет в список пресетов.\n
  --update, -u      Выкачивает последние изменения в присетах.\n
  --delete, -d      Удаляет пресет.\n
  --list, -l           Выводит список локально доступных пресетов.
""")

    if clone:
        os.chdir(presetDir)
        subprocess.call(['git', 'clone', clone])

    if update:
        os.chdir(presetDir)
        list = [os.path.join(presetDir, o) for o in os.listdir(presetDir)
                    if os.path.isdir(os.path.join(presetDir, o))]

        i = 0
        while i < len(list):
            click.secho('Обнавляется ' + list[i], fg='green')
            os.chdir(list[i])
            subprocess.call(['git', 'pull'])
            i += 1

    if delete:
        if os.path.exists(presetDir + '/' + delete):
            print (delete)
            subprocess.call(['rm', '-rf', presetDir + '/' + delete])
            click.secho(value + ' удален', fg='yellow')
        else:
            click.echo('нет такого пресета')
            value = listPresets(True)
            subprocess.call(['rm', '-rf', presetDir + '/' + value])
            click.secho(value + ' удален', fg='yellow')

    if list:
        listPresets()