import subprocess
def open():
    cmd_file_path = 'port1_on.cmd'
    subprocess.call(cmd_file_path, shell=True)

def close():
    cmd_file_path = 'port1_off.cmd'
    subprocess.call(cmd_file_path, shell=True)

# open()
# close()