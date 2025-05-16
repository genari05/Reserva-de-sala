from flask import Flask
from database import db
from controller.reserva_router import reserva_blueprint

app = Flask(__name__, instance_relative_config=True)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(reserva_blueprint)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
