import sbz_data


def load_config():
    with open("./sbzswitcher.conf") as configs:
        for config in configs:
            if config.startswith("#"):
                continue
            keyword, value = config.split("=")
            apply_config(keyword, value)


def apply_config(key, value):
    if key == "headphones_volume":
        sbz_data.set_headphones_volume(value)
    if key == "speakers_volume":
        sbz_data.set_speakers_volume(value)