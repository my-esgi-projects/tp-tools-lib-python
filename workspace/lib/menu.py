#!/usr/bin/python3

dict_menus = {
    "1": {
        "label": "1. Display OS Informations",
        "submenu": {
            "1": {
                "label": "\t 1. Show os name",
                "action": "os_name",
                "final": "The os name is : ",
            },
            "2": {
                "label": "\t 2. Show os architecture",
                "action": "os_architecture",
                "final": "The architecture of os is : ",
            },
            "3": {
                "label": "\t 3. Show os release",
                "action": "os_release",
                "final": "The release of os is : ",
            },
            "4": {
                "label": "\t 4. Show os hostname",
                "action": "os_hostname",
                "final": "The hostname is : ",
            },
            "0": {"label": "\t 0. Back to main menu", "action": "back_to_main_menu"},
        },
    },
    "2": {
        "label": "2. Display CPU Informations",
        "submenu": {
            "1": {
                "label": "\t 1. Show cpu name",
                "action": "cpu_name",
                "final": "CPU Name is : ",
            },
            "2": {
                "label": "\t 2. Show cpu architecture",
                "action": "cpu_architecture",
                "final": "CPU Architecture is : ",
            },
            "3": {
                "label": "\t 3. Percentage of cpu usage",
                "action": "cpu_percentage_usage",
                "final": "CPU Percentage used is : ",
            },
            "0": {
                "label": "\t 0. Back to main menu",
                "action": "back_to_main_menu",
            },
        },
    },
    "3": {
        "label": "3. Display Informations About Sensors",
        "submenu": {
            "1": {
                "label": "\t 1. Show battery information",
                "action": "sensors_battery",
                "final": "Battery is : ",
            },
            "2": {
                "label": "\t 2. Show sensors temperature",
                "action": "sensors_temperature",
                "final": "Temperature are : ",
            },
            "0": {"label": "\t 0. Back to main menu", "action": "back_to_main_menu"},
        },
    },
    "4": {
        "label": "4. Display Informations About Memory",
        "submenu": {
            "1": {
                "label": "\t 1. Show total memory size",
                "action": "memory_total",
                "final": "Total memory size in MB is : ",
            },
            "2": {
                "label": "\t 2. Show memory available",
                "action": "memory_available",
                "final": "Memory available in MB is : ",
            },
            "3": {
                "label": "\t 3. Show used memory",
                "action": "memory_used",
                "final": "Memory used in MB is : ",
            },
            "0": {"label": "\t 0. Back to main menu", "action": "back_to_main_menu"},
        },
    },
    "0": {
        "label": "0. Quit application",
        "submenu": {
            "yes": {
                "label": "\t Are you sure to quit ?(yes/no)",
                "action": "exit_application",
            },
            "no": {
                "label": "",
                "action": "client_menu",
            },
        },
    },
}
