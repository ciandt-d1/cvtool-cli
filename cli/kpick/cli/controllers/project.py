import os

import yaml
from cement.ext.ext_argparse import ArgparseController, expose

import kingpick_api_client
from kingpick_api_client.rest import ApiException

# create an instance of the API class
kingpick_api_client.configuration.host = 'https://kingpick-dev.scanvas.me/v1'
kingpick_api_client.configuration.debug = False
api_instance = kingpick_api_client.ProjectApi()


class ProjectController(ArgparseController):
    class Meta:
        label = 'project'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = "Manages Projects"
        epilog = "the text at the bottom of --help."        

    # @expose(hide=True)
    def default(self):
        self.app.args.print_help()

    @expose(
        help='List all projects',
        arguments=[
            (['-t', '--tenant_id'],
                dict(help='tenant id', action='store', dest='tenant_id')),
        ]        
    )
    def list(self):
        try:
            if self.app.pargs.tenant_id is None:
                try:
                    config_file = os.path.expanduser('~/.%s/config.yaml' % self.app._meta.label)
                    stream = open(config_file, 'r')
                    data = yaml.load(stream)
                    if 'default_tenant' in data.keys():
                        self.app.pargs.tenant_id = data['default_tenant']
                    else:
                        print('Missing tenant parameter (-t)')
                        return None
                except Exception as e:
                    print('Error: %s\n' % e)

            api_response = api_instance.list_projects(self.app.pargs.tenant_id)
            headers = ['ID', 'NAME', 'DESCRIPTION']
            data = [[t.id, t.name, t.description] for t in api_response.items]
            self.app.render(data, headers=headers)
            return data
        except ApiException as e:
            print("Exception when calling ProjectApi->list_projects: %s\n" % e)


    @expose(
        help='Creates a new Project',
        arguments=[
            (['-t', '--tenant_id'],
                dict(help='tenant id', action='store', dest='tenant_id')),
            (['-i', '--id'],
                dict(help='project id', action='store', dest='id')),
            (['-n', '--name'],
                dict(help='project name', action='store', dest='name')),
            (['-d', '--description'],
                dict(help='project description', action='store', dest='description')),
        ]        
    )
    def create(self):
        if self.app.pargs.tenant_id is None:
            try:
                config_file = os.path.expanduser('~/.%s/config.yaml' % self.app._meta.label)
                stream = open(config_file, 'r')
                data = yaml.load(stream)
                if 'default_tenant' in data.keys():
                    self.app.pargs.tenant_id = data['default_tenant']
                else:
                    print('Missing tenant parameter (-t)')
                    return None
            except Exception as e:
                print('Error: %s\n' % e)
        if self.app.pargs.id is None:
            print('Missing project id parameter (-i)')
            return None
        if self.app.pargs.name is None:
            print('Missing project name parameter (-n)')
            return None
        if self.app.pargs.description is None:
            print('Missing project description parameter (-d)')
            return None

        project = kingpick_api_client.Project()  # Project | Project to create
        project.id = self.app.pargs.id
        project.name = self.app.pargs.name
        project.description = self.app.pargs.description
        try: 
            api_response = api_instance.create_project(self.app.pargs.tenant_id, project)
            print("Created:\n%s" % api_response)
        except ApiException as e:
            print("Exception when calling TenantApi->create_tenant: %s\n" % e)
