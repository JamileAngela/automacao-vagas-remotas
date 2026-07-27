import requests


def buscar_vagas():
    vagas = []

    url = "https://www.arbeitnow.com/api/job-board-api"

    try:
        resposta = requests.get(url, timeout=30)
        resposta.raise_for_status()

        dados = resposta.json()

        for vaga in dados.get("data", []):

            vagas.append({
                "titulo": vaga.get("title", ""),
                "empresa": vaga.get("company_name", ""),
                "descricao": vaga.get("description", ""),
                "modelo": "Remoto" if vaga.get("remote") else "Presencial",
                "link": vaga.get("url", ""),
                "fonte": "Arbeitnow"
            })

    except Exception as erro:
        print("Erro:", erro)

    return vagas
