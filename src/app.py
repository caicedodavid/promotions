import click
import coverage
import os
import sys
import unittest
from project import create_app


if os.environ.get('FLASK_ENV') == 'development':
    COV = coverage.coverage(
        branch=True,
        include='*/project/*',
        omit=[
            '*/project/__init__.py',
            '*/project/_tests/*',
            '*/project/*/_tests/*',
            '*/project/views.py'
        ]
    )
    COV.start()


app = create_app()


@app.cli.command()
@click.option('--file', default='project')
def test(file: str) -> None:
    """Runs the tests without code coverage."""
    result = __run_tests(file)
    if result.wasSuccessful():
        sys.exit(0)

    sys.exit(1)


def __run_tests(file: str = 'project'):
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    if os.path.isdir(file):
        suite.addTests(loader.discover(
                file, pattern='test_*.py'))
    else:
        suite.addTests(loader.discover(
                'project', pattern=f'{file}.py'))

    return unittest.TextTestRunner(verbosity=2).run(suite)


@app.cli.command()
def cov() -> None:
    tests = unittest.TestLoader().discover('project', pattern='test_*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report(show_missing=True)
        COV.html_report()
        COV.erase()
        sys.exit(0)
    sys.exit(1)


if __name__ == '__main__':
    app.cli()
