import os
import unittest


from flask_testing import TestCase
from project import create_app


app = create_app()


class TestDevelopmentConfig(TestCase):
    """Test Development Config"""

    def create_app(self) -> None:
        app.config.from_object('project.configs.DevelopmentConfig')
        return app

    def test_config(self) -> None:
        """Ensure Development config is right"""
        self.assertFalse(app.config['TESTING'])
        self.assertTrue(app.config['DEBUG'])
        self.assertFalse(app.config['SQLALCHEMY_TRACK_MODIFICATIONS'])
        self.assertFalse(app.config['PRESERVE_CONTEXT_ON_EXCEPTION'])
        self.assertEqual(
            app.config['SQLALCHEMY_DATABASE_URI'],
            os.environ.get('DATABASE_URL'))
        self.assertTrue(app.config['SQLALCHEMY_ECHO'])


class TestTestingConfig(TestCase):
    """Test Testing Config"""

    def create_app(self) -> None:
        app.config.from_object('project.configs.TestingConfig')
        return app

    def test_config(self) -> None:
        """Ensure Testing config is right"""
        self.assertTrue(app.config['TESTING'])
        self.assertTrue(app.config['DEBUG'])
        self.assertFalse(app.config['SQLALCHEMY_TRACK_MODIFICATIONS'])
        self.assertFalse(app.config['PRESERVE_CONTEXT_ON_EXCEPTION'])
        self.assertEqual(
            app.config['SQLALCHEMY_DATABASE_URI'],
            f'{os.environ.get("DATABASE_URL")}_test')
        self.assertFalse(app.config['SQLALCHEMY_ECHO'])


class TestStagingConfig(TestCase):
    """Test Staging Config"""

    def create_app(self) -> None:
        app.config.from_object('project.configs.StagingConfig')
        return app

    def test_config(self) -> None:
        """Ensure Staging config is right"""
        self.assertFalse(app.config['TESTING'])
        self.assertTrue(app.config['DEBUG'])
        self.assertFalse(app.config['SQLALCHEMY_TRACK_MODIFICATIONS'])
        self.assertFalse(app.config['PRESERVE_CONTEXT_ON_EXCEPTION'])
        self.assertEqual(
            app.config['SQLALCHEMY_DATABASE_URI'],
            os.environ.get('DATABASE_URL'))
        self.assertFalse(app.config['SQLALCHEMY_ECHO'])


class TestProductionConfig(TestCase):
    """Test Production Config"""

    def create_app(self) -> None:
        app.config.from_object('project.configs.ProductionConfig')
        return app

    def test_config(self) -> None:
        """Ensure Production config is right"""
        self.assertFalse(app.config['TESTING'])
        self.assertFalse(app.config['DEBUG'])
        self.assertFalse(app.config['SQLALCHEMY_TRACK_MODIFICATIONS'])
        self.assertFalse(app.config['PRESERVE_CONTEXT_ON_EXCEPTION'])
        self.assertEqual(
            app.config['SQLALCHEMY_DATABASE_URI'],
            os.environ.get('DATABASE_URL'))
        self.assertFalse(app.config['SQLALCHEMY_ECHO'])


if __name__ == '__main__':
    unittest.main()
