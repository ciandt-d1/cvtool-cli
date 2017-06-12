"""kingpick-cli main application entry point."""
import os

from cement.core.exc import FrameworkError, CaughtSignal
from cement.core.foundation import CementApp
from cement.utils import fs
from cement.utils.misc import init_defaults

from kpick.core import exc

# Application default.  Should update config/kpick.yaml to reflect any
# changes, or additions here.
defaults = init_defaults('kpick')


# defaults['kpick']['api_host'] = 'https://kingpick-dev.scanvas.me'
# # All internal/external plugin configurations are loaded from here
# defaults['kpick']['plugin_config_dir'] = '/etc/kpick/plugins.d'
#
# # External plugins (generally, do not ship with application code)
# defaults['kpick']['plugin_dir'] = '/var/lib/kpick/plugins'
#
# # External templates (generally, do not ship with application code)
# defaults['kpick']['template_dir'] = '/var/lib/kpick/templates'


class App(CementApp):
    class Meta:
        label = 'kpick'
        extensions = ['yaml', 'tabulate', 'json']
        output_handler = 'tabulate'
        config_handler = 'yaml'
        config_extension = '.yaml'
        config_files = [
            os.path.join('/', 'etc', label, '%s%s' % (label, config_extension)),
            os.path.join(fs.HOME_DIR, '.%s%s' % (label, config_extension)),
            os.path.join(fs.HOME_DIR, '.%s' % label, 'config'),
            os.path.join(fs.HOME_DIR, '.%s' % label, 'config%s' % config_extension),
        ]

        config_defaults = defaults

        # All built-in application bootstrapping (always run)
        bootstrap = 'kpick.cli.bootstrap'

        # Internal plugins (ship with application code)
        plugin_bootstrap = 'kpick.cli.plugins'

        # Internal templates (ship with application code)
        template_module = 'kpick.cli.templates'

        # call sys.exit() when app.close() is called
        exit_on_close = True


class TestApp(App):
    """A test app that is better suited for testing."""

    class Meta:
        # default argv to empty (don't use sys.argv)
        argv = []

        # don't look for config files (could break tests)
        config_files = []

        # don't call sys.exit() when app.close() is called in tests
        exit_on_close = False


# Define the application object outside of main, as some libraries might wish
# to import it as a global (rather than passing it into another class/func)
app = App()


def main():
    with app:
        try:
            app.run()

        except exc.Error as e:
            # Catch our application errors and exit 1 (error)
            print('Error > %s' % e)
            app.exit_code = 1

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('CaughtSignal > %s' % e)
            app.exit_code = 0

        except FrameworkError as e:
            # Catch framework errors and exit 1 (error)
            print('FrameworkError > %s' % e)
            app.exit_code = 1

        finally:
            # Maybe we want to see a full-stack trace for the above
            # exceptions, but only if --debug was passed?
            if app.debug:
                import traceback
                traceback.print_exc()


if __name__ == '__main__':
    main()
