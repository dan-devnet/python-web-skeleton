from pathlib import Path
from helpers.config_helpers import CONF, PATH, BASE_DIR
# Absolute Paths starts with an /
# Config Items are defined by (<value>, <placeholder in configuration>)
# The placeholder can be used in Configurations: <<Placeholder>> and is replaced by the value


PROJECT             = CONF("py_001", "PROJECT-ID")
DIR_BASE            = BASE_DIR + "/"

DIR_APP_ROOT        = CONF("app/", "DIR_APP_ROOT", PATH)
DIR_VENV            = CONF("venv_" +str(PROJECT) + "/", "DIR_VENV", PATH)
DIR_APP             = CONF("app/app/", "DIR_APP", PATH)
DIR_MEDIA           = CONF("app/app/media/", PATH)

APP_GIT_REPO        = CONF("https://github.com/dan-devnet/dan-dev-wiki.git")

CONFIG_TEMPLATES    = CONF("build_maintainance/server_templates/", "", PATH)

# Absolute PATH required
DIR_SERVER_CONFIGS = CONF(str(DIR_BASE)+ "build_maintainance/server/","", PATH)
#_CONFIG_NGINX        = CONF()
#_CONFIG_NGINX_SERVER = CONF()
FILE_UWSGI_APP     = CONF("app.wsgi:application", "FILE_UWSGI_APP")
FILE_UWSGI_CONFIG  = CONF(str(DIR_SERVER_CONFIGS)+ "uwsgi.ini","", PATH)
#_CONFIG_UWSGI_PARAMS = CONF("","UWSGI_PARAMS", PATH)


NGINX_USR           = CONF("nginx", "NGINX_USR")
NGINX_GRP           = CONF("www-data", "NGINX_GRP")

UWSGI_USR           = CONF("uwsgi", "UWSGI_USR")
UWSGI_GRP           = CONF("www-data", "UWSGI_GRP")

UWSGI_PROCESSES     = CONF("auto", )


SERVER_NAME         = CONF("localhost", "SERVER_NAME")# CONF("dan-dev.net")
SERVER_PORT         = CONF("8080", "SERVER_PORT")
SOCKET_PATH         = CONF("app/app.sock", "SOCKET_PATH", PATH)



#_DIR_SSL_Keys       = CONF("/", "_DIR_SSL_KEYS", PATH)
_DIR_LOGS           = CONF("/var/logs/" + str(PROJECT) + "/", "_DIR_LOGS", PATH)

FILE_REQUIREMENTS   = CONF(str(DIR_APP_ROOT) + "requirements.txt")
