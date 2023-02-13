import subprocess

def turn_off_screen():
    subprocess.call('xset dpms force off', shell=True)

turn_off_screen()
