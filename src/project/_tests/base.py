from flask import current_app as app
from flask_injector import FlaskInjector
from flask_testing import TestCase


class BaseTestCase(TestCase):
    def configure_injector(self, binder):
        pass

    def create_app(self) -> None:
        app.config.from_object('project.configs.TestingConfig')
        FlaskInjector(
            app=app,
            modules=[self.configure_injector],
            injector=app.config.get('injector')
        )
        return app
