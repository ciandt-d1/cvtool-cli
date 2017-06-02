import json
import os

import httplib2
import oauth2client.clientsecrets as clientsecrets
import oauth2client.file as oauthfile
import oauth2client.tools as oauthtools
import yaml
from cement.ext.ext_argparse import ArgparseController, expose
from cement.utils import shell
from cement.utils.misc import minimal_logger
from oauth2client.client import flow_from_clientsecrets


LOG = minimal_logger(__name__)

CONFIG_FILE = 'config.yaml'
CREDENTIALS_FILE = 'credentials.json'
SCOPES = ['email', 'https://www.googleapis.com/auth/cloud-platform']
CLIENT_SECRETS_FILE = 'client_secrets.json'
CLIENT_SECRETS = {
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

class InitController(ArgparseController):

    class Meta:
        label = 'init'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = "Initialize or reinitialize %s" % 'teste'
        # arguments = [
        #     (['-m', '--message'],
        #      dict(help='message', action='store', dest='msg')),
        # ]

    @expose(help="Initialize or reinitialize", hide=True)
    def default(self):
        #p = shell.Prompt("Press Enter To Continue", default='ENTER')
        CONFIG_DIR = os.path.expanduser('~/.%s/' % self.app._meta.label)
        ensure_dir(CONFIG_DIR)

        client_secrets_file = os.path.join(CONFIG_DIR, CLIENT_SECRETS_FILE)
        with open(client_secrets_file, 'w') as outfile:
            json.dump(CLIENT_SECRETS, outfile)

        flow = flow_from_clientsecrets(client_secrets_file, SCOPES)
        storage = oauthfile.Storage(os.path.join(CONFIG_DIR, CREDENTIALS_FILE))
        credentials = storage.get()
        if credentials is None or credentials.invalid:
            credentials = oauthtools.run_flow(flow, storage, WebFlowFlags())
        else:
            http = httplib2.Http()
            http = credentials.authorize(http)
            credentials.refresh(http)

        id_token = credentials.token_response.get('id_token')
        h = httplib2.Http()
        (resp_headers, content) = h.request("https://kingpick-dev.scanvas.me/api/auth/v1/token", "GET", headers={'Authorization':'Bearer '+id_token })
        config_file = os.path.join(CONFIG_DIR, CONFIG_FILE)
        data = dict(
            id_token = id_token,
            access_token = content.decode('utf-8')
        )
        with open(config_file, 'w') as outfile:
            yaml.safe_dump(data, outfile, default_flow_style=False)


def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)


class WebFlowFlags(object):

    def __init__(self):
        self.noauth_local_webserver = False

    @property
    def logging_level(self):
        return 'ERROR'

    @property
    def noauth_local_webserver(self):
        return self._noauth_local_webserver

    @noauth_local_webserver.setter
    def noauth_local_webserver(self, value): 
        self._noauth_local_webserver = value

    @property
    def auth_host_port(self):
        return [8080, 8090]

    @property
    def auth_host_name(self):
        return 'localhost'