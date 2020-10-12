
# nginx config1 > config location
# nginx config2 > sites-available
# syslink ln nginx sites-enabled < sites-available

# generate uswgi config in defined location ? which?

# SSL Generation
from helpers.config_helpers import CONF
from config import CONFIG_TEMPLATES, DIR_BASE, PROJECT, FILE_UWSGI_CONFIG, DIR_VENV

def setup_server():
    create_config_files()
    #setup_nginx()
    #setup_uwsgi()
    #setup_daemon()
    #start()

def create_config_files():
    gconfig  = CONF()
    #print(gconfig.get_all_config_items_representation())
    #print("BASE_DIR:" + str(DIR_BASE))
    gconfig.apply_placeholders( str(CONFIG_TEMPLATES) + "uwsgi.ini", str(DIR_BASE) + "server/uwsgi.ini")
    gconfig.apply_placeholders( str(CONFIG_TEMPLATES) + "nginx_config_server.conf", DIR_BASE + "server/nginx_" + str(PROJECT) + ".conf")
    gconfig.apply_placeholders( str(CONFIG_TEMPLATES) + "nginx.conf", str(DIR_BASE) + "server/nginx.conf")
    gconfig.apply_placeholders( str(CONFIG_TEMPLATES) + "uwsgi.conf", str(DIR_BASE) + "server/uwsgi.conf")

def setup_uwsgi():
    print("setup uwsgi")
    collectstatic = ("source {}/bin/activate && python3 manage.py collectstatic").format(DIR_VENV)
    collectstatic_log = subprocess.getoutput(collectstatic)
    startuwsgi = ("source {}/bin/activate && uwsgi --ini " + str(FILE_UWSGI_CONFIG)).format(DIR_VENV)
    collectstatic_log = subprocess.getoutput(collectstatic)
    dbmigrate = ("source {}/bin/activate && python3 manage.py migrate").format(DIR_VENV)
    dbmigrate_log = subprocess.getoutput(dbmigrate)
    createsuperuser = ("source {}/bin/activate && python3 manage.py createsuperuser").format(DIR_VENV)
    createsuperuser_log = subprocess.getoutput(creatsuperuser)

def setup_nginx():
    print("is your nginx running?")

def setup_daemon():
    print("setup uwsgi daemon")
    #https://uwsgi-docs.readthedocs.io/en/latest/Emperor.html

def start():
    print("start_server")

if __name__ == '__main__':
    setup_server()
