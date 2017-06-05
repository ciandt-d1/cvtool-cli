import os

import yaml
from cement.ext.ext_argparse import ArgparseController, expose

from .base import ApiClientMixin


class ImageController(ApiClientMixin, ArgparseController):
    class Meta:
        label = 'image'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = "Manages images"
        epilog = "the text at the bottom of --help."

    # @expose(hide=True)
    def default(self):
        self.app.args.print_help()

    @expose(
        help='Export images to Big Query',
        arguments=[
            (['-t', '--tenant'],
             dict(help='', action='store', dest='tenant'))
        ]
    )
    def export(self):
        tenant_id = self.app.pargs.tenant
        if tenant_id is None:
            config_file = os.path.expanduser('~/.%s/config.yaml' % self.app._meta.label)
            stream = open(config_file, 'r')
            data = yaml.load(stream)
            if 'default_tenant' in data.keys():
                tenant_id = data['default_tenant']
            else:
                print('Missing tenant parameter (-t)')
                return None
        self.api_client.image.export(tenant_id)
