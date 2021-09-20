import subprocess

# 'PRIVATE' VARIABLES
__headphones_volume = 0
__speakers_volume = 0


def get_sbz_id():
    process = subprocess.Popen(["sh", "scripts/sbz_id.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    sbz_id = out.decode("ascii").replace("\n", "")
    return sbz_id


# HEADPHONES VOLUME GETTERS AND SETTERS
def set_headphones_volume(volume):
    # Write volume in config file
    #
    global __headphones_volume
    __headphones_volume = float(volume)

    if get_current_output_device()[0] == "values=1":
        set_master_volume(__headphones_volume)


def get_headphones_volume():
    return __headphones_volume


# SPEAKERS VOLUME GETTERS AND SETTERS
def set_speakers_volume(volume):
    # Write volume in config file
    #
    global __speakers_volume
    __speakers_volume = float(volume)

    if get_current_output_device()[0] == "values=0":
        set_master_volume(__speakers_volume)


def get_speakers_volume():
    return __speakers_volume


def set_master_volume(volume):
    if 100 >= volume >= 0:
        cmd = r"amixer sset 'Master' " + str(volume) + "%"
        __run_command(cmd)


def get_current_output_device():
    # output = 0 ----> Speakers
    # output = 1 ----> Headphones
    cmd = r"amixer -c " + str(get_sbz_id()) + " cget numid=36 | grep -E -o 'values=[0-9]$'"

    return __run_command(cmd)


# 'PRIVATE' FUNCTIONS
def __run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    return out.decode("ascii").replace("\n", ""), err.decode("ascii").replace("\n", "")
