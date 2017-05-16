from cement.ext.ext_argparse import ArgparseController, expose

import time
import kingpick_api_client
from kingpick_api_client.rest import ApiException
from pprint import pprint

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

    @expose(hide=True)
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
            api_response = api_instance.list_projects(self.app.pargs.tenant_id)
            pprint(api_response)
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
        project = kingpick_api_client.Project() # Project | Project to create
        project.id = self.app.pargs.id
        project.name = self.app.pargs.name
        project.description = self.app.pargs.description
        try: 
            api_response = api_instance.create_project(self.app.pargs.tenant_id, project)
        except ApiException as e:
            print("Exception when calling TenantApi->create_tenant: %s\n" % e)
