import subprocess
import os
from build_vars import DIR_BASE, DIR_APP

choice = input("!!! WARNING !!! This will delete all files in the app directory! Continue? [y] or [n]")

if (choice == 'y'):
    os.system("rm -rf " + DIR_APP + "/*")
    git_repo = input("Git-repo-URL:")
    command = "git init && git clone " + git_repo + " " + str(DIR_APP)
    git_pull_debug = subprocess.getoutput(command)
    print(git_pull_debug)
