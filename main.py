import requests

print("Robô de vagas iniciado!")

url = "https://api.github.com/repos/python/cpython"

resposta = requests.get(url)

dados = resposta.json()

print("Projeto encontrado:")
print(dados["name"])
print("Estrelas:")
print(dados["stargazers_count"])
