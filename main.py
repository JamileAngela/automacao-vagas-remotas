from limpeza import remover_duplicadas
from fontes.adzuna import buscar_vagas
from classificador import classificar_vaga


print("🔎 Buscando oportunidades...\n")


buscas = [
    "logística remoto",
    "customer service remoto",
    "suporte remoto",
    "python remoto",
    "java remoto",
    "inteligência artificial remoto",
    "edição vídeo remoto"
]


todas_vagas = []


for busca in buscas:

    print("Buscando:", busca)

    vagas = buscar_vagas(busca)

    todas_vagas.extend(vagas)



# Agora sim remove duplicadas
todas_vagas = remover_duplicadas(todas_vagas)


print("\nTotal encontrado:", len(todas_vagas))


for vaga in todas_vagas[:20]:

    titulo = vaga.get("title", "")
    descricao = vaga.get("description", "")

    resultado = classificar_vaga({
        "titulo": titulo,
        "descricao": descricao
    })


    print("----------------------------")
    print("Título:", titulo)
    print("Empresa:", vaga.get("company", {}).get("display_name"))


    if resultado:

        print("Compatibilidade:")

        for perfil in resultado:
            print(
                "-",
                perfil["perfil"],
                "| Pontos:",
                perfil["pontuacao"]
            )

    else:

        print("Sem perfil identificado")


    print("Link:", vaga.get("redirect_url"))
