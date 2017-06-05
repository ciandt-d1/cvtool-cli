"""kingpick-cli bootstrapping."""

# All built-in application controllers should be imported, and registered
# in this file in the same way as BaseController.
from kpick.cli.controllers.base import BaseController
from kpick.cli.controllers.init import InitController
from kpick.cli.controllers.tenant import TenantController
from kpick.cli.controllers.project import ProjectController
from kpick.cli.controllers.job import JobController
from kpick.cli.controllers.image import ImageController


def load(app):
    app.handler.register(BaseController)
    app.handler.register(InitController)
    app.handler.register(TenantController)
    app.handler.register(ProjectController)
    app.handler.register(JobController)
    app.handler.register(ImageController)
