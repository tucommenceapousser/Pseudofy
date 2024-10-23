from flask import Flask

def Create_Apps():
    app = Flask(__name__)
    from .routes import main
    app.register_blueprint(main)

    return app