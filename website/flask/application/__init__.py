from flask import Flask
from flask_failsafe import failsafe



@failsafe
def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Include our Routes
        from .similar import similar
        from .images import images



        # Register Blueprints
        app.register_blueprint(similar.similar_bp)
        app.register_blueprint(images.images_bp)
        return app