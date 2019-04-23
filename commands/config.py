# -*- coding: utf-8 -*-

import os
import click
import json

env = os.environ
directory = env['HOME'] + '/.front-cli'


def getConfig():
    os.chdir(directory)
    with open('conf.json', 'r') as file:
        return json.load(file)

def setConfig(data):
    with open('conf.json', 'w') as file:
        json.dump(data, file, sort_keys=True, indent=4)

def parseJsonToStr(data):
    return json.dumps(data, sort_keys=True, indent=4)

@click.command()
@click.option('--sql-user', default=False, help='Замена юзера')
@click.option('--sql-password', default=False, help='Замена пароля')
@click.option('--root-dir', default=False, help='Замена корневой директории проектов')
@click.option('--list', '-l', is_flag=True, help='Показать конфиг')
def config(sql_user, sql_password, root_dir, list):
    """Служит для редактирования конфига"""
    click.echo((sql_user, sql_password, root_dir, list))

    if sql_user:
        click.secho(sql_user, fg='green')
        user = getConfig()
        user['mysql']['login'] = sql_user
        setConfig(user)

    if sql_password:
        click.secho(sql_password, fg='green')
        password = getConfig()
        password['mysql']['password'] = sql_password
        setConfig(password)

    if root_dir:
        click.echo('none')
        click.secho(root_dir, fg='green')

    if list:
        click.secho('{}'.format(parseJsonToStr(getConfig())), fg='green')