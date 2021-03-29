import subprocess


def create_script(interpreter, script):
    subprocess.run(f"{interpreter} {script}", shell=True)
    return
