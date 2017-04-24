"""CLI tests for kpick."""

from kpick.utils import test

class CliTestCase(test.TestCase):
    def test_kpick_cli(self):
        argv = ['--foo=bar']
        with self.make_app(argv=argv) as app:
            app.run()
            self.eq(app.pargs.foo, 'bar')
