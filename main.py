import requests

print("🔎 Buscando oportunidades reais...")

url = "https://www.arbeitnow.com/api/job-board-api"

try:
    resposta = requests.get(url, timeout=30)
    resposta.raise_for_status()

    dados = resposta.json()
    vagas = dados["data"][:10]  # Primeiras 10 vagas

    print(f"\n{len(vagas)} oportunidades encontradas:\n")

    for vaga in vagas:

        titulo = vaga.get("title", "Sem título")
        empresa = vaga.get("company_name", "Empresa não informada")
        remoto = "Remoto" if vaga.get("remote", False) else "Não remoto"
        link = vaga.get("url", "")

        print("----------------------------")
        print("Título:", titulo)
        print("Empresa:", empresa)
        print("Modelo:", remoto)
        print("Link:", link)

except Exception as erro:
    print("Erro:", erro)
