# -*- coding: utf-8 -*-

import os
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