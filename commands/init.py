# -*- coding: utf-8 -*-

import os
import click
import subprocess
from common import getConfig, controlDir, listPresets, copyPreset, getProjectCWD

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

def npmInstall(path):
    if os.path.exists(path + '/package.json'):
        try:
            subprocess.call('yarn')
        except:
            try:
                subprocess.call(['npm', 'install'])
            except:
                click.secho('Node.js не установлет')

def composerInstall(path, name):
    print((path, name))
    if os.path.exists(path + '/' + name + '/.env.example'):
        os.chdir(path + '/' + name)
        subprocess.call(['cp', path + '/' + name + '/.env.example', path + '/' + name + '/.env'])

        with open('.env.example', 'r') as file:
            old_data = file.read()

        new_data = old_data.replace('DB_DATABASE=homestead', 'DB_DATABASE=' + name)
        new_data = new_data.replace('DB_USERNAME=homestead', 'DB_USERNAME=' + conf['mysql']['user'])
        new_data = new_data.replace('DB_PASSWORD=secret', 'DB_PASSWORD=' + conf['mysql']['password'])
        new_data = new_data.replace('MAIL_DRIVER=smtp', 'MAIL_DRIVER=log')

        with open('.env', 'w') as file:
            file.write(new_data)

        # try:
        #     subprocess.call(['composer', 'install'])
        # except:
        #     click.secho('Composer не установлен')

@click.command()
# @click.option('--clone', '-c', default=False, help='Клонирование репозитория')
# @click.option('--update', '-u', is_flag=True, help='Выкачивает последние изменения в присетах.')
# @click.option('--delete', '-d', default=False, help='Удаляет пресет.')
@click.option('--npm-install', '-i', is_flag=True)
@click.argument('name', nargs=-1)
def init(name, npm_install):
    """Разворачивает новый проект из пресета"""

#     click.secho('\nОпции команды init', fg='green', bold=True)
#     click.echo("""  --clone, -c       Добавляет пресет в список пресетов.\n
#   --update, -u      Выкачивает последние изменения в присетах.\n
#   --delete, -d      Удаляет пресет.\n
#   --list, -l           Выводит список локально доступных пресетов.
# """)

    if name != ():
        if checking(name[0]):
            preserName = listPresets(True)
            copyPreset(name[0], preserName)
            npmInstall(getProjectCWD() + '/' + name[0])
            composerInstall(getProjectCWD(), name[0])

    elif name == () and npm_install:
        click.echo('active option')
        npmInstall(os.getcwd())

    else:
        name = raw_input('Название проекта: ')

        if checking(name):
            preserName = listPresets(True)
            copyPreset(name, preserName)
            npmInstall(getProjectCWD() + '/' + name)
            composerInstall(getProjectCWD(), name)
