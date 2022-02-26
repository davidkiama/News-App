from flask import Flask
from .config import DevConfig


# Initialize the app
app = Flask(__name__)
# Import config
app.config.from_object(DevConfig)


from app import views
