from flask import Flask, render_template
from models import db
from api import bp as api_bp
import os


def create_app(test_config=None):
    app = Flask(__name__, template_folder='templates')
    db_path = os.path.join('/tmp', 'spools.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)

    if test_config:
        app.config.update(test_config)

    db.init_app(app)
    app.register_blueprint(api_bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
