
# nginx config1 > config location
# nginx config2 > sites-available
# syslink ln nginx sites-enabled < sites-available

# generate uswgi config in defined location ? which?

# SSL Generation
from helpers.config_helpers import CONF
from config import CONFIG_TEMPLATES, DIR_BASE, PROJECT

def setup_server():
    create_config_files()



def create_config_files():
    gconfig  = CONF()
    print(gconfig.get_all_config_items_representation())
    print("BASE_DIR:" + str(DIR_BASE))
    gconfig.apply_placeholders( str(CONFIG_TEMPLATES) + "uwsgi.ini", str(DIR_BASE) + "server/uwsgi.ini")
    gconfig.apply_placeholders( str(CONFIG_TEMPLATES) + "nginx_config_server.conf", DIR_BASE + "server/nginx_" + str(PROJECT) + ".conf")
    gconfig.apply_placeholders( str(CONFIG_TEMPLATES) + "nginx.conf", str(DIR_BASE) + "server/nginx.conf")

if __name__ == '__main__':
    setup_server()
