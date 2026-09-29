from flask import Flask

from config import Config
from database import db
from controller.employee_controller import (
    employee_controller
)


def create_app():

    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Initialize SQLAlchemy
    db.init_app(app)

    # Register controller
    app.register_blueprint(
        employee_controller
    )

    return app


if __name__ == "__main__":

    app = create_app()

    app.run(
        host="localhost",
        port=5000,
        debug=True
    )