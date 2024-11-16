"""
app/__init__.py
"""

from flask import Flask

def create_app():
    """
    Create a Flask application instance.
    """
    app = Flask(__name__)

    @app.route('/hello')
    def hello():
        return 'Welcome to Market Place!'

    from .home import home_bp
    app.register_blueprint(home_bp, url_prefix='/home')

    return app
