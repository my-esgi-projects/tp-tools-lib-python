#!/usr/bin/python
# coding: utf-8

import platform, psutil, cpuinfo
from lib.menu import dict_menus

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
    return cpuinfo.get_cpu_info()["brand_raw"]


def cpu_architecture():
    return platform.architecture()[0]


def cpu_percentage_usage():
    cpu_percentage = psutil.cpu_percent(interval=1)
    return f"{str(cpu_percentage)}%"


def count_logical_cpu():
    logical_cpu = psutil.cpu_count(logical=True)
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
    choices = tuple(concat_choices.split("_"))
    function_name = dict_menus[choices[0]]["submenu"][choices[1]]["action"]
    return eval(function_name)()


"""
    capteurs informations
"""


def sensors_battery():
    battery = psutil.sensors_battery()
    return str(
        f"{int(battery.percent)}% {'charging' if battery.power_plugged else 'not in charge'}"
    )


def sensors_temperature():
    sensors_temperature = psutil.sensors_temperatures()["acpitz"]
    current, high, critical = 0, 0, 0
    for data in sensors_temperature:
        current += data.current if data.current != None else 0
        high += data.high if data.high != None else 0
        critical += data.critical if data.critical != None else 0

    current, high, critical = (
        current / len(sensors_temperature),
        high / len(sensors_temperature),
        critical / len(sensors_temperature),
    )

    return str(f"current={current}°C, high={high}°C, critical={critical}°C")
