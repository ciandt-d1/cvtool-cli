import cvtool_cli_client as client
from ..cli.main import app

USER_AGENT = 'cvtool-cli/1.0'

Tenant = client.Tenant
Job = client.Job


class CliRestClient(object):

    @staticmethod
    def _client():
        app_name = app.args.prog
        host = app.config.get(app_name, 'api_host')
        access_token = app.config.get(app_name, 'access_token')
        client.configuration.access_token = access_token
        api_client = client.ApiClient(host=host + '/v1')
        api_client.user_agent = USER_AGENT
        return api_client

    @property
    def tenants(self):
        return client.TenantApi(api_client=self._client())

    @property
    def projects(self):
        return client.ProjectApi(api_client=self._client())

    @property
    def images(self):
        return client.ImageApi(api_client=self._client())

    @property
    def jobs(self):
        return client.JobApi(api_client=self._client())


class AuthRestClient(object):
    def __init__(self, host, debug=False):
        client.configuration.debug = debug
        self._host = host

    def token(self, id_token):
        api_client = client.ApiClient(host=self._host + '/v1')
        client.configuration.access_token = id_token
        api_client.user_agent = USER_AGENT
        return client.AuthApi(api_client=api_client).token()

    @classmethod
    def from_app(cls, app):
        app_name = app.args.prog
        host = app.config.get(app_name, 'api_host')
        return cls(host=host, debug=app.debug)
