"""kingpick-cli bootstrapping."""

# All built-in application controllers should be imported, and registered
# in this file in the same way as BaseController.

from kpick.cli.controllers import *


def load(app):
    app.handler.register(BaseController)
    app.handler.register(InitController)
    app.handler.register(AuthController)
    app.handler.register(TenantController)
    app.handler.register(ProjectController)
    app.handler.register(JobController)
    app.handler.register(ImageController)
    app.handler.register(AuthController)
