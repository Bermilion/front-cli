# -*- coding: utf-8 -*-

import os
import click
import json

env = os.environ
directory = env['HOME'] + '/.front-cli'
presetDir = env['HOME'] + '/.front-cli/presets'

def getConfig():
    os.chdir(directory)
    with open('conf.json', 'r') as file:
        return json.load(file)

def setConfig(data):
    with open('conf.json', 'w') as file:
        json.dump(data, file, sort_keys=True, indent=4)

def parseJsonToStr(data):
    return json.dumps(data, sort_keys=True, indent=4)

def controlDir(path, name):
    if os.path.exists(path + '/' + name):
        click.secho('Директория ' + str(name) + ' существует', fg='red')
        return False
    else:
        os.mkdir(path + '/' + name)
        click.secho('Директория ' + str(name) + ' создана', fg='green')
        return True

def echoList(list):
    i = 0
    while i < len(list):
        presetName = list[i].split('/')[len(list[i].split('/')) - 1]
        click.secho('[' + str(i) + '] — ' + presetName, fg='green')
        i += 1

def listPresets(select=False):
    list = [os.path.join(presetDir, o) for o in os.listdir(presetDir)
        if os.path.isdir(os.path.join(presetDir, o))]

    if select:
        echoList(list)
        value = int(raw_input('Введите значение: '))
        print (list[value].split('/')[len(list[value].split('/')) - 1])
        return list[value].split('/')[len(list[value].split('/')) - 1]
    else:
        click.secho('Доступные пресеты', fg='green')
        echoList(list)
        return list