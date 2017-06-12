import json
import os

import httplib2
import oauth2client.file as oauthfile
import oauth2client.tools as oauthtools
from oauth2client.client import flow_from_clientsecrets

from kpick.cli.main import app
from kpick.core import configuration, api

CREDENTIALS_FILE = 'credentials.json'
SCOPES = ['email']
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


def login():

    if not configuration.exists():
        print('Configuration file does not exist try the "init" command first')
        return

    client_secrets_file = os.path.join(configuration.CONFIG_DIR, CLIENT_SECRETS_FILE)
    with open(client_secrets_file, 'w') as outfile:
        json.dump(CLIENT_SECRETS, outfile)

    flow = flow_from_clientsecrets(client_secrets_file, SCOPES)
    storage = oauthfile.Storage(os.path.join(configuration.CONFIG_DIR, CREDENTIALS_FILE))
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        credentials = oauthtools.run_flow(flow, storage, WebFlowFlags())
    else:
        http = httplib2.Http()
        http = credentials.authorize(http)
        credentials.refresh(http)

    id_token = credentials.token_response.get('id_token')
    auth_api = api.AuthRestClient.from_app(app)
    access_token = auth_api.token(id_token)
    configuration.update(id_token, access_token)


class WebFlowFlags(object):
    def __init__(self):
        self.noauth_local_webserver = True

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
