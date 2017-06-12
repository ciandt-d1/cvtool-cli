import urllib

from cement.ext.ext_argparse import ArgparseController, expose
from cement.utils.shell import Prompt

from kpick.core import configuration
from kpick.core.auth import login

WELCOME_MESSAGE = """Welcome! This command will take you through the configuration of cvtool.

Your settings will be saved to {}.

"""
ASK_FOR_LOGIN_MSG = "To continue, you must login. Would you like to login now?"


class LoginPrompt(Prompt):
    class Meta:
        text = ASK_FOR_LOGIN_MSG
        options = ['Y', 'n']
        options_separator = '|'
        default = 'Y'
        clear = False

        # def process_input(self):
        #     if self.input.lower() == 'y':
        #         auth = AuthController()
        #         auth.login()
        #     else:
        #         print("User doesn't agree! I'm outta here")
        #         sys.exit(1)


class ApiServerUriPrompt(Prompt):
    class Meta:
        default = 'https://api.cvtool.com'
        text = "What's the API server uri [{}] ?".format(default)
        clear = False
        auto = False

    def process_input(self):
        if not is_valid(self.input):
            print('Please enter a valid URI')
            self.input = None


class InitController(ArgparseController):
    class Meta:
        label = 'init'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = "Initialize or reinitialize %s" % 'teste'

    @expose(help="Initialize or reinitialize", hide=True)
    def default(self):

        self.app.log.debug('%s does not exist. Initializing.'.format(configuration.CONFIG_FILE))
        print(WELCOME_MESSAGE.format(configuration.CONFIG_FILE))

        api_server_uri_prompt = ApiServerUriPrompt()
        while api_server_uri_prompt.input is None:
            api_server_uri_prompt.prompt()

        configuration.create(api_uri=api_server_uri_prompt.input)
        self.app.config.merge(configuration.get())

        login_prompt = LoginPrompt()
        if login_prompt.input.lower() == 'y':
            login()


min_attributes = ('scheme', 'netloc')


def is_valid(url, qualifying=None):
    qualifying = min_attributes if qualifying is None else qualifying
    token = urllib.parse.urlparse(url)
    return all([getattr(token, qualifying_attr)
                for qualifying_attr in qualifying])
