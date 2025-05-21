
from flask import request
from database import db
from datetime import datetime
import requests

from flask import request, from database import db
import requests
from sqlalchemy import Date, Time
from datetime import datetime


class Reserva(db.Model):
    __tablename__ = 'reservas'

    id = db.Column(db.Integer, primary_key=True)
    turma_id = db.Column(db.Integer, nullable=False)
    sala = db.Column(db.String(50), nullable=False)

    data = db.Column(db.String(20), nullable=False)         # Ex: "2025-06-01"
    hora_inicio = db.Column(db.String(10), nullable=False)  # Ex: "08:00"
    hora_fim = db.Column(db.String(10), nullable=False)      # Ex: "10:00"

# Função para listar todas as reservas
def listar_reservas():
    reservas = Reserva.query.all()
    return [
        {
            "id": reserva.id,
            "turma_id": reserva.turma_id,
            "sala": reserva.sala,
            "data": reserva.data,
            "hora_inicio": reserva.hora_inicio,
            "hora_fim": reserva.hora_fim
        } for reserva in reservas
    ]

# Validação real via requisição HTTP ao microserviço de turmas
def validar_turma(turma_id):
    try:
        resp = requests.get(f"http://turmas_service:5000/api/turmas/{turma_id}")
        return resp.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Erro ao validar turma: {e}")
        return False

# Criação de reserva
def criar_reserva():
    dados = request.json

=======
    data = db.Column(db.String(20), nullable=False)  # possivel ateração para date 
    hora_inicio = db.Column(db.String(10), nullable=False)  # possivel ateração para time
    hora_fim = db.Column(db.String(10), nullable=False)     # possivel ateração para time


def validar_turma(turma_id):
    try:
        resp = requests.get(f"http://localhost:5000/api/turmas/{turma_id}")
        return resp.status_code == 200
    except requests.exceptions.RequestException:
        return False


def criar_reserva():
    dados = request.json

    # Verifica campos obrigatórios -- posiveol ateração para try except 

    obrigatorios = ["turma_id", "sala", "data", "hora_inicio", "hora_fim"]
    faltando = [campo for campo in obrigatorios if not dados.get(campo)]
    if faltando:
        return {"erro": f"Campos obrigatórios ausentes: {', '.join(faltando)}"}, 400

    turma_id = dados.get("turma_id")


    if not validar_turma(turma_id):
        return {"erro": "Turma não encontrada"}, 400


    
    if not validar_turma(turma_id):
        return {"erro": "Turma não encontrada"}, 400

    

    reserva = Reserva(
        turma_id=turma_id,
        sala=dados.get("sala"),
        data=dados.get("data"),
        hora_inicio=dados.get("hora_inicio"),
        hora_fim=dados.get("hora_fim")
    )


    try:
        db.session.add(reserva)
        db.session.commit()
        return {"mensagem": "Reserva criada com sucesso"}, 201
    except Exception as e:
        db.session.rollback()
        return {"erro": "Erro ao salvar no banco de dados", "detalhes": str(e)}, 500



def listar_reservas():
    reservas = Reserva.query.all()
    return [
        {
            "id": r.id,
            "turma_id": r.turma_id,
            "sala": r.sala,
            "data": r.data,
            "hora_inicio": r.hora_inicio,
            "hora_fim": r.hora_fim
        } for r in reservas
    ]

