from flask import current_app as app
from flask_injector import FlaskInjector
from flask_testing import TestCase

from project import db


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

    def setUp(self) -> None:
        db.create_all()
        db.session.commit()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
