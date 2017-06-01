import datetime
import json
import os

import dateutil.parser
import requests
import time

import yaml
from cement.ext.ext_argparse import ArgparseController, expose

import kingpick_api_client
from kingpick_api_client.rest import ApiException

# create an instance of the API class
kingpick_api_client.configuration.host = 'https://kingpick-dev.scanvas.me/v1'
kingpick_api_client.configuration.debug = False
api_instance = kingpick_api_client.TenantApi()


class ImageController(ArgparseController):
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
        try:
            if self.app.pargs.tenant is None:
                try:
                    config_file = os.path.expanduser('~/.%s/config.yaml' % self.app._meta.label)
                    stream = open(config_file, 'r')
                    data = yaml.load(stream)
                    if 'default_tenant' in data.keys():
                        self.app.pargs.tenant = data['default_tenant']
                    else:
                        print('Missing tenant parameter (-t)')
                        return None
                except Exception as e:
                    print('Error: %s\n' % e)

            api_response = requests.post(
                kingpick_api_client.configuration.host + '/images/' + self.app.pargs.tenant + '/export', data='')
            print(api_response.text)
        except Exception as e:
            print("Error: %s\n" % e)
