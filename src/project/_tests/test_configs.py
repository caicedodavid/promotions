import os
import unittest


from flask_testing import TestCase
from project import create_app


app = create_app()


class TestConfig(TestCase):
    """Test Development Config"""

    def create_app(self) -> None:
        app.config.from_object('project.configs.DevelopmentConfig')
        return app

    def test_config(self) -> None:
        """Ensure Development config is right"""
        self.assertFalse(app.config['TESTING'])
        self.assertTrue(app.config['DEBUG'])
        self.assertFalse(app.config['PRESERVE_CONTEXT_ON_EXCEPTION'])
