
from flask import Blueprint, request, jsonify
from model.reserva_model import *
from database import db

import requests

reserva_blueprint = Blueprint("reserva_routes", __name__, url_prefix="/reserva")


# Função interna para verificar se a turma existe
def validar_turma(turma_id):
    try:
        resp = requests.get(f"http://localhost:5000/turmas/{turma_id}")
        return resp.status_code == 200
    except requests.RequestException:
        return False


# ROTA 1: Criar uma nova reserva
@reserva_blueprint.route("/", methods=["POST"])
def criar_reserva():
    dados = request.json
    turma_id = dados.get("turma_id")

    if not validar_turma(turma_id):
        return jsonify({"erro": "Turma não encontrada"}), 400

    reserva = Reserva(
        turma_id=turma_id,
        sala=dados.get("sala"),
        data=dados.get("data"),
        hora_inicio=dados.get("hora_inicio"),
        hora_fim=dados.get("hora_fim")
    )

    db.session.add(reserva)
    db.session.commit()

    return jsonify({"mensagem": "Reserva criada com sucesso"}), 201

# ROTA 2: Listar todas as reservas
@reserva_blueprint.route("/", methods=["GET"])
def listar_reservas():
    reservas = Reserva.query.all()
    return jsonify([
        {
            "id": r.id,
            "turma_id": r.turma_id,
            "sala": r.sala,
            "data": r.data,
            "hora_inicio": r.hora_inicio,
            "hora_fim": r.hora_fim
        } for r in reservas
    ])

# ROTA 3: Verificar se uma turma existe (isoladamente)
@reserva_blueprint.route("/validar_turma/<int:turma_id>", methods=["GET"])
def validar_turma_router(turma_id):
    resultado = validar_turma(turma_id)
    return jsonify({"valida": resultado})

=======
from flask import Blueprint, request, jsonify
from model.reserva_model import *
from database import db
import requests

routes = Blueprint("routes", __name__)


def validar_turma(turma_id):
        pass


@routes.route("/reservas", methods=["POST"])
def criar_reserva():
    create_reserva = criar_reserva()
    return jsonify(create_reserva)


@routes.route("/reservas", methods=["GET"])
def listar_reservas():
    list_reserva = listar_reservas()
    return jsonify(list_reserva)

