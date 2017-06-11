import datetime
import os
import time

import dateutil.parser
import yaml
from cement.ext.ext_argparse import ArgparseController, expose

# create an instance of the API class
from .base import ApiClientMixin


class JobController(ApiClientMixin, ArgparseController):
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

        def datetime_to_local_timezone(dt):
            epoch = dt.timestamp()
            st_time = time.localtime(epoch)
            tz = datetime.timezone(datetime.timedelta(
                seconds=st_time.tm_gmtoff))
            return dt.astimezone(tz)

        tenant_id = self.app.pargs.tenant
        job_id = self.app.pargs.job_id

        if tenant_id is None:
            try:
                config_file = os.path.expanduser('~/.%s/config.yaml' % self.app._meta.label)
                stream = open(config_file, 'r')
                data = yaml.load(stream)
                if 'default_tenant' in data.keys():
                    tenant_id = data['default_tenant']
                else:
                    print('Missing tenant parameter (-t)')
                    return None
            except Exception as e:
                print('Error: %s\n' % e)

        if job_id is None:
            print('Missing job id parameter (-i)')
            return None

        while True:

            job = self.api_client.jobs.get(tenant_id, job_id)

            headers = ['ID', 'STARTED', 'ENDED', 'IMAGE COUNT', 'STATUS']
            data = [[j.get('id', '-'),
                     datetime_to_local_timezone(dateutil.parser.parse(j['start_time']))
                         .strftime('%d/%m/%Y %H:%M:%S') if 'start_time' in j else '-',
                     datetime_to_local_timezone(dateutil.parser.parse(j['end_time']))
                         .strftime('%d/%m/%Y %H:%M:%S') if 'end_time' in j else '-',
                     j.get('image_count', '-'), j.get('status', '-')] for j in [response_data]]
            os.system('clear')
            self.app.render(data, headers=headers)

            if job.status == 'FINISHED':
                break

            print('Updated at: ' + datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
            time.sleep(1)

        # always return the data, some output handlers require this
        # such as Json/Yaml (which don't use templates)
        return data

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
        tenant_id = self.app.pargs.tenant
        if tenant_id is None:
            try:
                config_file = os.path.expanduser('~/.%s/config.yaml' % self.app._meta.label)
                stream = open(config_file, 'r')
                data = yaml.load(stream)
                if 'default_tenant' in data.keys():
                    tenant_id = data['default_tenant']
                else:
                    print('Missing tenant parameter (-t)')
                    return None
            except Exception as e:
                print('Error: %s\n' % e)
        if self.app.pargs.csv is None:
            print('Missing csv parameter (-c)')
            return None

        data = {
            'type': 'csv',
            'auto_start': True,
            'input_params': {
                'csv_uri': self.app.pargs.csv,
                'vision_api_features': 'LANDMARK_DETECTION,LOGO_DETECTION,LABEL_DETECTION,IMAGE_PROPERTIES'
            }
        }
        job = self.api_client.jobs.create(tenant_id, data)
        print(job.id)
