from fontes.adzuna import buscar_vagas
from classificador import classificar_vaga


print("🔎 Buscando oportunidades reais...\n")


try:

    vagas = buscar_vagas()

    print(f"{len(vagas)} vagas recebidas\n")


    for vaga in vagas:

        titulo = vaga.get("title", "Sem título")
        empresa = vaga.get("company", {}).get("display_name", "Empresa não informada")
        descricao = vaga.get("description", "")
        link = vaga.get("redirect_url", "")


        vaga_formatada = {
            "titulo": titulo,
            "descricao": descricao
        }


        perfis = classificar_vaga(vaga_formatada)


        print("----------------------------")
        print("Título:", titulo)
        print("Empresa:", empresa)


        if perfis:

            print("Perfis compatíveis:")

            for perfil in perfis:
                print(
                    "-",
                    perfil["perfil"],
                    "| Pontos:",
                    perfil["pontuacao"]
                )

        else:

            print("Sem perfil identificado")


        print("Link:", link)


except Exception as erro:

    print("Erro:", erro)
