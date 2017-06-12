from cement.ext.ext_argparse import ArgparseController, expose

import kpick.core.auth as authenticator


class AuthController(ArgparseController):
    class Meta:
        label = 'auth'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = 'Triggers the authentication flow'

    @expose(help="Initialize or reinitialize", hide=False)
    def login(self):
        authenticator.login()


