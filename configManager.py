import sbz_data
from pathlib import Path

__config_structure = ["headphones_volume=16",
                    "speakers_volume=68"]

__missing_properties = []


def create_config_file():
    with open("sbzswitcher.conf", "w") as file:
        for cfg in __config_structure:
            file.write(cfg)
            file.write("\n")


def load_config():
    with open("sbzswitcher.conf", "r") as configs:
        for config in configs:
            if config.startswith("#"):
                continue
            try:
                keyword, value = config.split("=")
            except ValueError as e:
                continue
            apply_config(keyword, value)


def apply_config(key, value):
    if key == "headphones_volume":
        sbz_data.set_headphones_volume(value)
    if key == "speakers_volume":
        sbz_data.set_speakers_volume(value)


def check_config_file():

    path = Path("sbzswitcher.conf")
    if not path.is_file():
        # File doesn't exist
        create_config_file()
        print("Config file doesn't exist.\nCreating new config file")
    else:
        if not config_file_is_ok():
            print("There are missing properties in configuration file.")
            # Fill missing properties
            fill_missing_properties()

    load_config()


def config_file_is_ok():
    state = True

    with open("sbzswitcher.conf", "r") as file:
        file_content = ""

        for line in file.readlines():
            file_content += line

        for cfg in __config_structure:
            prop = cfg.split("=")[0]
            if prop not in file_content:
                print("Property missing: " + prop)
                __missing_properties.append(prop)
                state = False
    return state


def fill_missing_properties():
    with open("sbzswitcher.conf", "a") as file:

        for mp in __missing_properties:
            for prop in __config_structure:
                if mp in prop:
                    file.write(prop)
                    file.write("\n")


