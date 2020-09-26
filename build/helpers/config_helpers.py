#sudo service nginx reload
#sudo service nginx restart
import os
import fileinput
from pathlib import Path

BASE_DIR = str(Path(__file__).resolve().parent.parent.parent)
PLACEHOLDER_START = "<<"
PLACEHOLDER_END = ">>"
PATH = 1

class CONF:
    ITEMS = []
    is_initialized = False

    def __init__(self, value=None, placeholder=None, type=None):
        self.value = str(value)
        self.placeholder = (PLACEHOLDER_START + str(placeholder) + PLACEHOLDER_END)
        self.type = type
        # Convert Relative to absolute Paths
        if self.type == PATH:
            if not self.value.startswith('/'):
                os.path.join(BASE_DIR, self.value)
        if value != None and placeholder != None:
            self.__class__.ITEMS.append({'value':self.value, 'placeholder':self.placeholder})

    def __str__(self):
        return self.value

    def get_all_config_items_representation(self):
        config_item_view = ""
        for config_item in self.__class__.ITEMS:
            config_item_view += ("\n" + str(config_item['placeholder']) + " => " + str(config_item['value']))
        return config_item_view

    def apply_placeholders(self, path_src_file, path_dst_file):
        # Read in the file
        with open(path_src_file, 'r') as file :
            filedata = file.read()
            # Replace the target string
            for placeholder in self.__class__.ITEMS:
                filedata = filedata.replace(placeholder['placeholder'], placeholder['value'])
        # Write the file out again
        with open(path_dst_file, 'w') as file:
            file.write(filedata)
