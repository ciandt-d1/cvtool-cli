import os

import yaml
from cement.ext.ext_argparse import ArgparseController, expose

from .base import ApiClientMixin
from ...core import api


class TenantController(ApiClientMixin, ArgparseController):
    class Meta:
        label = 'tenant'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = "Manages tenants"
        epilog = "the text at the bottom of --help."

    # @expose(hide=True)
    def default(self):
        self.app.args.print_help()

    @expose(help='List all tenants')
    def list(self):
        self.app.log.debug('Listing tenants')
        api_response = self.api_client.tenants.get_tenants()

        headers = ['ID', 'NAME', 'DESCRIPTION']
        data = [[t.id, t.name, t.description] for t in api_response.items]
        self.app.render(data, headers=headers)

        # always return the data, some output handlers require this
        # such as Json/Yaml (which don't use templates)
        return data

    @expose(
        help='Creates a new tenant',
        arguments=[
            (['-i', '--id'],
             dict(help='tenant id', action='store', dest='id')),
            (['-n', '--name'],
             dict(help='tenant name', action='store', dest='name')),
            (['-d', '--description'],
             dict(help='tenant description', action='store', dest='description')),
            (['--google-cloud-project'],
             dict(help='google cloud project where resources (storage, bigquery, etc) will be allocated ', action='store', dest='google_cloud_project')),
            (['--staging-bucket'],
             dict(help='GCS bucket for temporary files', action='store', dest='gcs_staging_bucket')),
        ]
    )
    def create(self):

        if self.app.pargs.id is None:
            print('Missing tenant id parameter (-i)')
            return None
        if self.app.pargs.name is None:
            print('Missing tenant name parameter (-n)')
            return None
        if self.app.pargs.google_cloud_project is None:
            print('Missing tenant google-cloud-project parameter (--google-cloud-project)')
            return None
        if self.app.pargs.gcs_staging_bucket is None:
            print('Missing tenant staging-bucket parameter (--staging-bucket)')
            return None

        tenant = api.Tenant()
        tenant.id = self.app.pargs.id
        tenant.name = self.app.pargs.name
        tenant.description = self.app.pargs.description
        tenant.settings = dict(
            google_cloud_project=self.app.pargs.google_cloud_project,
            gcs_staging_bucket=self.app.pargs.gcs_staging_bucket,
        )

        api_response = self.api_client.tenants.post_tenant(tenant)
        print("Created:\n%s" % api_response)

    @expose(
        help='Set default tenant',
        arguments=[
            (['-i', '--id'],
             dict(help='tenant id', action='store', dest='id'))
        ]
    )
    def set_default(self):
        if self.app.pargs.id is None:
            print('Missing tenant id parameter (-i)')
            return None
        config_file = os.path.expanduser('~/.%s/config.yaml' % self.app._meta.label)
        stream = open(config_file, 'r')
        data = yaml.load(stream)
        data['default_tenant'] = self.app.pargs.id
        with open(config_file, 'w') as yaml_file:
            yaml_file.write(yaml.dump(data, default_flow_style=False))

    @expose(help='Get default tenant')
    def get_default(self):
        config_file = os.path.expanduser('~/.%s/config.yaml' % self.app._meta.label)
        stream = open(config_file, 'r')
        data = yaml.load(stream)
        if 'default_tenant' in data.keys():
            print('default-tenant=%s' % data['default_tenant'])
        else:
            print('No default tenant')
