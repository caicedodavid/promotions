import os
import marshmallow
import werkzeug
from flask import Flask, jsonify
from flask_cors import CORS
from flask_injector import FlaskInjector
from flask_marshmallow import Marshmallow
from flask_mongoengine import MongoEngine

mongo = MongoEngine()
ma = Marshmallow()


def format_error_response(message, status: int) -> dict:
    return {
        'status': status,
        'detail': message
    }


def register_error_handlers(app):
    @app.errorhandler(marshmallow.exceptions.ValidationError)
    def validation_error_handler(ex):
        return jsonify(format_error_response(ex.messages, 400)), 400

    @app.errorhandler(werkzeug.exceptions.BadRequest)
    @app.errorhandler(werkzeug.exceptions.Unauthorized)
    @app.errorhandler(werkzeug.exceptions.Forbidden)
    @app.errorhandler(werkzeug.exceptions.NotFound)
    @app.errorhandler(werkzeug.exceptions.MethodNotAllowed)
    @app.errorhandler(werkzeug.exceptions.InternalServerError)
    @app.errorhandler(Exception)
    def json_error_handler(e: Exception) -> tuple:
        if isinstance(e, werkzeug.exceptions.HTTPException):
            message = format_error_response(e.description, e.code)
            return jsonify(message), e.code

        message = format_error_response(str(e), 500)
        return jsonify(message), 500


def register_routes(app):
    from project.routes import register
    register(app)


def create_app():
    app = Flask(__name__)
    app_config = os.getenv('APP_CONFIG')
    app.config.from_object(app_config)
    CORS(app)
    ma.init_app(app)
    mongo.init_app(app)

    register_routes(app)
    register_error_handlers(app)
    from project.binder import configure
    # Do all the dependecy injection and store the injector in the config
    flask_injector = FlaskInjector(app=app, modules=[configure])
    app.config.update({'injector': flask_injector.injector})
    return app
