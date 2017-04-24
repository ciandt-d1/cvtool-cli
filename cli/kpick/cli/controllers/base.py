"""kingpick-cli base controller."""

from cement.ext.ext_argparse import ArgparseController, expose


VERSION = '0.1.0'

BANNER = """
Kingpick Computer Vision Tool v%s
Copyright (c) 2017 D1
""" % VERSION


class BaseController(ArgparseController):
    class Meta:
        label = 'base'
        description = 'Kingpick CLI client - computer vision tool'
        arguments = [
            (['-t', '--tenant'],
             dict(help='the tenant id', dest='tenant', action='store',
                  metavar='TEXT') ),
             (['-v', '--version'], dict(action='version', version=BANNER)),      
            ]

    @expose(hide=True)
    def default(self):
        self.app.args.print_help()
        # print("Inside BaseController.default().")

        # If using an output handler such as 'mustache', you could also
        # render a data dictionary using a template.  For example:
        #
        #   data = dict(foo='bar')
        #   self.app.render(data, 'default.mustache')
        #
        #
        # The 'default.mustache' file would be loaded from
        # ``kpick.cli.templates``, or ``/var/lib/kpick/templates/``.
        #
