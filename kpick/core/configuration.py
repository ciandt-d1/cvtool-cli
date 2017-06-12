import os

import yaml
from ..cli.main import app


CONFIG_DIR = os.path.expanduser('~/.%s/' % app._meta.label)
CONFIG_FILE = os.path.join(CONFIG_DIR, 'config.yaml')


def _ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)


def exists():
    return os.path.exists(CONFIG_FILE)


def get():
    with open(CONFIG_FILE, 'r+') as outfile:
        return yaml.safe_load(outfile)


def create(api_uri=None, id_token=None, access_token=None, debug=False):
    _ensure_dir(CONFIG_DIR)
    data = dict(
        kpick=dict(
            debug=debug,
            api_host=api_uri,
            id_token=id_token,
            access_token=access_token
        )
    )
    with open(CONFIG_FILE, 'w') as outfile:
        yaml.safe_dump(data, outfile, default_flow_style=False)


def update(id_token, access_token):
    with open(CONFIG_FILE, 'r+') as outfile:
        data = yaml.safe_load(outfile)
        import copy
        new_data = copy.deepcopy(data)
        new_data[app._meta.label]['id_token'] = id_token
        new_data[app._meta.label]['access_token'] = access_token

    with open(CONFIG_FILE, 'w') as outfile:
        yaml.safe_dump(new_data, outfile, default_flow_style=False)
