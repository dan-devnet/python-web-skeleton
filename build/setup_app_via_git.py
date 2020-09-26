import subprocess
import os
from config import DIR_BASE, DIR_APP

def setup_app_via_git():
    choice = input("!!! WARNING !!! This will delete all files in the app directory! Continue? [y] or [n]")

    if (choice == 'y'):
        os.system("rm -rf " + DIR_APP + "/*")
        git_repo = input("Git-repo-URL:")
        command = "git init && git clone " + git_repo + " " + str(DIR_APP)
        git_pull_debug = subprocess.getoutput(command)
        print(git_pull_debug)

if __name__ == '__main__':
    setup_app_via_git()
