import subprocess
# This is used to execute terminal commands in python scripts.
for i in range(5):
    subprocess.check_call(['python', 'example.py'])