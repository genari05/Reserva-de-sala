# services/turma_client.py
import requests

TURMA_SERVICE_URL = "http://turmas_service:5000/api/turmas"

def turma_existe(turma_id):
    try:
        resp = requests.get(f"{TURMA_SERVICE_URL}/{turma_id}")
        return resp.status_code == 200
    except requests.RequestException as e:
        print(f"Erro ao conectar com serviço de turmas: {e}")
        return False
