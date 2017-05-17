import json
import os

import requests
from cement.ext.ext_argparse import ArgparseController, expose

import kingpick_api_client
from kingpick_api_client.rest import ApiException

# create an instance of the API class
kingpick_api_client.configuration.host = 'https://kingpick-dev.scanvas.me/v1'
kingpick_api_client.configuration.debug = False
api_instance = kingpick_api_client.TenantApi()


class JobController(ArgparseController):
    class Meta:
        label = 'job'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = "Manages jobs"
        epilog = "the text at the bottom of --help."

    # @expose(hide=True)
    def default(self):
        self.app.args.print_help()

    @expose(
        help='Info about the job',
        arguments=[
            (['-t', '--tenant'],
             dict(help='', action='store', dest='tenant')),
            (['-i', '--job_id'],
             dict(help='', action='store', dest='job_id'))
        ]
    )
    def info(self):
        try:
            if self.app.pargs.tenant is None:
                print('Missing tenant parameter (-t)')
                return None
            if self.app.pargs.job_id is None:
                print('Missing job id parameter (-i)')
                return None

            while True:
                api_response = requests.get(
                    kingpick_api_client.configuration.host +
                    '/jobs/' + self.app.pargs.job_id + '?tenant_id=' + self.app.pargs.tenant)

                response_data = json.loads(api_response.text)

                headers = ['ID', 'STARTED', 'ENDED', 'UPDATED', 'STATUS']
                data = [[j.get('id', '-'), j.get('start_time', '-'),
                         j.get('end_time', '-'), j.get('last_updated', '-'),
                         j.get('status', '-')] for j in [response_data]]
                os.system('clear')
                self.app.render(data, headers=headers)

                if response_data['status'] == 'FINISHED':
                    break

            # always return the data, some output handlers require this
            # such as Json/Yaml (which don't use templates)
            return data

        except ApiException as e:
            print("Exception when calling TenantApi->get_tenant: %s\n" % e)

    @expose(
        help='Creates a new job',
        arguments=[
            (['-c', '--csv'],
             dict(help='csv file path from a GCS bucket', action='store', dest='csv')),
            (['-t', '--tenant'],
             dict(help='tenant id', action='store', dest='tenant')),
            # (['-p', '--path'],
            #  dict(help='GCS bucket path', action='store', dest='path')),
        ]
    )
    def ingest(self):
        try:
            if self.app.pargs.tenant is None:
                print('Missing tenant parameter (-t)')
                return None
            if self.app.pargs.csv is None:
                print('Missing csv parameter (-c)')
                return None
            api_response = requests.post(
                kingpick_api_client.configuration.host +
                '/jobs?tenant_id=' + self.app.pargs.tenant + '&project_id=default_project',
                data=json.dumps({
                    'type': 'csv',
                    'auto_start': True,
                    'input_params': {
                        'csv_uri': self.app.pargs.csv,
                        'vision_api_features': 'LANDMARK_DETECTION,LOGO_DETECTION,LABEL_DETECTION,IMAGE_PROPERTIES'
                    }
                }),
                headers={'Content-Type': 'application/json'}
            )
            print(api_response.text)
        except ApiException as e:
            print("Exception when calling: %s\n" % e)
