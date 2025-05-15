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
