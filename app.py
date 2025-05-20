from flask import Flask
from database import db
from controller.reserva_router import reserva_blueprint

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')  # <- carrega as configs

db.init_app(app)
app.register_blueprint(reserva_blueprint)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )
