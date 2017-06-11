import json
import os

import sys
import yaml
from cement.ext.ext_argparse import ArgparseController, expose
from cement.utils import shell
from cement.utils.shell import Prompt


CONFIG_FILE = 'config.yaml'
CREDENTIALS_FILE = 'credentials.json'
SCOPES = ['email', 'https://www.googleapis.com/auth/cloud-platform']
CLIENT_SECRETS_FILE = 'client_secrets.json'

CLIENT_SECRETS_WEB = {
    "web": {
        "client_id": "1019062845561-ncr4dtvcshrrlg68nofsbmfnc7mf3g81.apps.googleusercontent.com",
        "project_id": "ciandt-cognitive-sandbox",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://accounts.google.com/o/oauth2/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_secret": "iVlVhvP7CeYfC-nwXfi0J-ol",
        "redirect_uris": [
            "http://localhost:8085/",
            "http://localhost:8090/",
            "http://localhost:8080/"
        ]
    }
}

CLIENT_SECRETS = {
    "installed": {
        "client_id": "1019062845561-ji7m6maafaueqf05li1b27vht5lgaebq.apps.googleusercontent.com",
        "project_id": "ciandt-cognitive-sandbox",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://accounts.google.com/o/oauth2/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_secret": "jKGlKDPsauX_oww7TjfEy7vi",
        "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob", "http://localhost"]
    }
}

WELCOME_MESSAGE = """Press Welcome! This command will take you through the configuration of cvtool."""

ASK_FOR_LOGIN_MSG = "To continue, you must login. Would you like to login ?"


class ApiServerUriPrompt(Prompt):
    class Meta:
        text = "Whats the API server uri ?"
        default = 'https://api.cvtool.com'
        clear = False

    def process_input(self):
        print(self.input)


class InitController(ArgparseController):
    class Meta:
        label = 'init'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = "Initialize or reinitialize %s" % 'teste'

    @expose(help="Initialize or reinitialize", hide=True)
    def default(self):

        config_dir = os.path.expanduser('~/.%s/' % self.app._meta.label)
        config_file = os.path.join(config_dir, CONFIG_FILE)
        if not os.path.exists(config_file):
            self.app.log.debug('%s does not exist. Initializing.'.format(config_file))
            p = ApiServerUriPrompt()
        else:
            self.app.log.debug('reinitializing')
            LoginPrompt()


def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)


