from flask import Flask, render_template
from models import db
from api import bp as api_bp


def create_app(test_config=None):
    app = Flask(__name__, template_folder='templates')
    app.config.setdefault('SQLALCHEMY_DATABASE_URI', 'sqlite:///spools.db')
    app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    if test_config:
        app.config.update(test_config)
    db.init_app(app)
    app.register_blueprint(api_bp)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        return render_template('index.html')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()

app = create_app()