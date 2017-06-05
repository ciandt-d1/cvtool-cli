"""kingpick-cli base controller."""

from cement.ext.ext_argparse import ArgparseController, expose

from kpick.core import api

VERSION = '0.1.1'

BANNER = """
Kingpick Computer Vision Tool v%s
Copyright (c) 2017 D1
""" % VERSION


class BaseController(ArgparseController):
    class Meta:
        label = 'base'
        description = 'Kingpick CLI client - computer vision tool'
        arguments = [(['-v', '--version'], dict(action='version', version=BANNER))]

    @expose(hide=True)
    def default(self):
        self.app.args.print_help()


class ApiClientMixin(object):

    def _setup(self, app):
        super(ApiClientMixin, self)._setup(app)
        self.api_client = api.CliRestClient.from_app(app)

