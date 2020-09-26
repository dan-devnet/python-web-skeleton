import os
import virtualenv
import subprocess

from pathlib import Path
from build_vars import DIR_BASE, DIR_REQUIREMENTS_TXT, DIR_VENV


def setup_venv():
    print('Creating environment using virtualenv [' + str(DIR_VENV) + ']...')
    virtualenv.cli_run([str(DIR_VENV)])
    print('Done!')

    print('Installing all required python packages via pip from' + str(DIR_REQUIREMENTS_TXT))
    pip_install = ("source {}/bin/activate && pip install -r " + str(DIR_REQUIREMENTS_TXT) + "/requirements.txt").format(DIR_VENV)
    pip_packages = ("source {}/bin/activate && pip freeze").format(DIR_VENV)
    pip_install_log = subprocess.getoutput(pip_install)
    pip_packages_installed = subprocess.getoutput(pip_packages)
    print('Installed packages:' + '\n' + pip_packages_installed)
    print('Done!')

if __name__ == '__main__':
    setup_venv()
