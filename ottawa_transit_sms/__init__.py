import enum

from flask import Flask

from ottawa_transit_sms import config

__version__ = "0.1.0"


class Environment(enum.Enum):
    TESTING = enum.auto()
    DEVELOPMENT = enum.auto()
    PRODUCTION = enum.auto()

    def from_string(env: str) -> "Environment":
        return getattr(Environment, env.strip().upper())


CONFIGMAP = {
    Environment.TESTING: config.TestingConfig,
    Environment.DEVELOPMENT: config.DevelopmentConfig,
    Environment.PRODUCTION: config.ProductionConfig,
}


def create_app(environment: Environment):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(CONFIGMAP[environment])
    app.config.from_pyfile("application.cfg", silent=True)

    from ottawa_transit_sms.sms_api import sms_blueprint

    app.register_blueprint(sms_blueprint)

    from ottawa_transit_sms.views import views

    app.register_blueprint(views)

    return app
