#!/usr/bin/python
# coding: utf-8

import platform, psutil, cpuinfo
from modules.client_utils import dict_menus

"""
    os informations
"""
def os_name():
    return platform.system()

def os_architecture():
    return platform.machine()

def os_release():
    return platform.release()

def os_hostname():
    return platform.node()


"""
    cpu informations
"""

def cpu_name():
    return cpuinfo.get_cpu_info()['brand_raw']

def cpu_architecture():
    return platform.architecture()[0]

def cpu_percentage_usage():
    cpu_percentage = psutil.cpu_percent(interval=1)
    return f'{str(cpu_percentage)}%'

def count_logical_cpu():
    logical_cpu =  psutil.cpu_count(logical=True)
    return logical_cpu


"""
    memory informations
"""
def memory_total():
    return str(psutil.virtual_memory().total / (1024 * 1024))

def memory_available():
    return str(psutil.virtual_memory().available / (1024 * 1024))

def memory_used():
    return str(psutil.virtual_memory().used / (1024 * 1024))


def function_output(concat_choices):
    choices = tuple(concat_choices.split('_'))
    print(choices)
    function_name = dict_menus[choices[0]]['submenu'][choices[1]]['action']
    function_object = globals()[function_name]
    return function_object()
