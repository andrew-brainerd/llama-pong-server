from app.api import bp as api_bp
from app import routes
from flask import Flask

app = Flask(__name__)


app.register_blueprint(api_bp, url_prefix='/api')
