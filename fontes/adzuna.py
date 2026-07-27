import requests

from config import ADZUNA_APP_ID, ADZUNA_APP_KEY


def buscar_vagas():

    url = "https://api.adzuna.com/v1/api/jobs/br/search/1"

    parametros = {
        "app_id": ADZUNA_APP_ID,
        "app_key": ADZUNA_APP_KEY,
        "results_per_page": 10,
        "what": "home office"
    }

    resposta = requests.get(
        url,
        params=parametros,
        timeout=30
    )

    resposta.raise_for_status()

    dados = resposta.json()

    return dados["results"]
