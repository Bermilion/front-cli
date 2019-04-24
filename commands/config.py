# -*- coding: utf-8 -*-

import os
import click
from common import getConfig, setConfig, parseJsonToStr

env = os.environ
directory = env['HOME'] + '/.front-cli'


@click.command()
@click.option('--sql-user', default=False, help='Замена пользователя')
@click.option('--sql-password', default=False, help='Замена пароля')
@click.option('--root-dir', default=False, help='Замена корневой директории проектов,\n если указан false использоваться не будет.')
@click.option('--list', '-l', is_flag=True, help='Показать конфиг')
def config(sql_user, sql_password, root_dir, list):
    """Служит для редактирования конфига"""

    click.secho('\nОпции команды config', fg='green', bold=True)
    click.echo("""  --sql-user      Замена пользователя\n
  --sql-password  Замена пароля\n
  --root-dir      Замена корневой директории проектов,\n                  если указан false использоваться не будет.\n
  --list          Вывести конфиг.
""")

    if sql_user:
        user = getConfig()
        user['mysql']['user'] = sql_user
        setConfig(user)

    if sql_password:
        password = getConfig()
        password['mysql']['password'] = sql_password
        setConfig(password)

    if root_dir:
        projects_dir = getConfig()
        projects_dir['root-dir'] = root_dir
        setConfig(projects_dir)

    if list:
        click.secho('{}'.format(parseJsonToStr(getConfig())), fg='green')