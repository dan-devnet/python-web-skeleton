import subprocess
import os
from config import DIR_BASE, DIR_APP, APP_GIT_REPO, DIR_APP_ROOT

def setup_app_via_git():
    choice = input("!!! WARNING !!! This will delete all files in the app directory! Continue? [y] or [n]")

    if (choice == 'y'):
        os.system("rm -rf " + str(DIR_APP_ROOT))
        command = "cd " + str(DIR_BASE) + " && git init && git clone " + str(APP_GIT_REPO) + " " + str(DIR_APP_ROOT)
        git_pull_debug = subprocess.getoutput(command)
        print(git_pull_debug)

if __name__ == '__main__':
    setup_app_via_git()
