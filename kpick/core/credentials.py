import os

import yaml
from ..cli.main import app


def _ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

CONFIG_DIR = os.path.expanduser('~/.%s/' % app._meta.label)
CONFIG_FILE = 'credentials.yaml'
config_file = os.path.join(CONFIG_DIR, CONFIG_FILE)

_ensure_dir(CONFIG_DIR)


def save(data):
    with open(config_file, 'w') as outfile:
        yaml.safe_dump(data, outfile, default_flow_style=False)


def load():
    with open(config_file, 'r') as outfile:
        yaml.safe_load(outfile)

def get_access_token():
    pass