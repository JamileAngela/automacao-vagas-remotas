print("Robô de vagas iniciado!")

vagas = [
    {
        "titulo": "Desenvolvedor Python Júnior",
        "empresa": "Empresa Exemplo",
        "localizacao": "Remoto",
        "link": "https://exemplo.com/vaga"
    },
    {
        "titulo": "Analista de Dados",
        "empresa": "Empresa Exemplo 2",
        "localizacao": "São Paulo",
        "link": "https://exemplo.com/vaga2"
    }
]


print("\nVagas encontradas:")

for vaga in vagas:
    print("--------------------")
    print("Título:", vaga["titulo"])
    print("Empresa:", vaga["empresa"])
    print("Local:", vaga["localizacao"])
    print("Link:", vaga["link"])
