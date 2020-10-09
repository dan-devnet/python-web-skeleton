import os
import virtualenv
import subprocess

from pathlib import Path
from config import DIR_BASE, FILE_REQUIREMENTS, DIR_VENV


def setup_venv():
    print('Creating environment using virtualenv [' + str(DIR_VENV) + ']...')
    virtualenv.cli_run([str(DIR_VENV)])
    print('Done!')

    print('Installing all required python packages via pip from: ' + str(FILE_REQUIREMENTS))
    pip_install = ("source {}/bin/activate && pip install -r " + str(FILE_REQUIREMENTS)).format(DIR_VENV)
    pip_packages = ("source {}/bin/activate && pip freeze").format(DIR_VENV)
    pip_install_log = subprocess.getoutput(pip_install)
    pip_packages_installed = subprocess.getoutput(pip_packages)
    print('Install...' + str(pip_install_log))
    print('Installed packages:' + '\n' + pip_packages_installed)
    print('Done!')

if __name__ == '__main__':
    setup_venv()
