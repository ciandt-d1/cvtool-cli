from cement.ext.ext_argparse import ArgparseController, expose

import time
import kingpick_api_client
from kingpick_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
kingpick_api_client.configuration.host = 'https://kingpick-dev.scanvas.me/v1'
kingpick_api_client.configuration.debug = False
api_instance = kingpick_api_client.TenantApi()


class TenantController(ArgparseController):
    class Meta:
        label = 'tenant'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = "Manages tenants"
        epilog = "the text at the bottom of --help."        

    @expose(hide=True)
    def default(self):
        self.app.args.print_help()

    # @expose(help='Changes tenant configuration')
    # def set_configuration(self):
    #     tenant_id = 'tenant_id_example' # str | tenant id
    #     tenant = kingpick_api_client.Tenant() # Tenant | Tenant to create

    #     try: 
    #         api_response = api_instance.post_tenant(tenant)
    #         pprint(api_response)
    #     except ApiException as e:
    #         print("Exception when calling TenantApi->get_tenant: %s\n" % e)


    @expose(help='List all tenants')
    def list(self):
        try: 
            api_response = api_instance.get_tenants()

            headers = ['ID', 'NAME', 'DESCRIPTION']
            data = [ [t.id, t.name, t.description] for t in api_response.items ]
            self.app.render(data, headers=headers)

            # always return the data, some output handlers require this
            # such as Json/Yaml (which don't use templates)
            return data
        except ApiException as e:
            print("Exception when calling TenantApi->get_tenant: %s\n" % e)


    @expose(
        help='Creates a new tenant',
        arguments=[
            (['-i', '--id'],
                dict(help='tenant id', action='store', dest='id')),
            (['-n', '--name'],
                dict(help='tenant name', action='store', dest='name')),
            (['-d', '--description'],
                dict(help='tenant description', action='store', dest='description')),
            # (['--source', '-s'],
            #     dict(help="Source Image Dataset Storage", dest='source')),
            # (['--dest', '-d'],
            #     dict(help="Destination ML Dataset Storage", dest='dest')),
            # (['--thumb', '-t'],
            #     dict(help="Image Dataset Thumbnail Storage", dest='thumb')),
            # (['--cloud-vision-key', '-v'],
            #     dict(help="API Keys for Cloud Vision", dest='cloud_vision_key')),
            # (['--cloud-ml-key', '-m'],
            #     dict(help="API Keys for Cloud ML", dest='cloud_ml_key'))
        ]        
    )
    def create(self):
        tenant = kingpick_api_client.Tenant() # Tenant | Tenant to create
        tenant.id = self.app.pargs.id
        tenant.name = self.app.pargs.name
        tenant.description = self.app.pargs.description
        try: 
            api_response = api_instance.post_tenant(tenant)
        except ApiException as e:
            print("Exception when calling TenantApi->create_tenant: %s\n" % e)
        
