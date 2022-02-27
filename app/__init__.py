from flask import Flask
from config import config_options


def create_app(config_name):
    # Initialize the app
    app = Flask(__name__)

    # Setting up config
    app.config.from_object(config_options[config_name])

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Setting up the config
    from .request import configure_request
    configure_request(app)

    print('*****************************************************************')
    print(app.config)

    return app
