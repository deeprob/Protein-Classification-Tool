import subprocess


def create_kernel_features(kernel_interpreter, kernel_script):
    subprocess.run(f"{kernel_interpreter} {kernel_script}", shell=True)
    return


def create_ifeatures(ifeature_interpreter, ifeature_script):
    subprocess.run(f"{ifeature_interpreter} {ifeature_script}", shell=True)
    return


def create_possum_features(possum_interpreter, possum_script):
    subprocess.run(f"{possum_interpreter} {possum_script}", shell=True)
    return
