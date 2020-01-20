#from app import app
from app.api import create_app, cli

app = create_app()
cli.register(app)