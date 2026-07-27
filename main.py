from fontes.adzuna import buscar_vagas


print("🔎 Testando Adzuna API...")


try:
    vagas = buscar_vagas()

    print(f"\n{len(vagas)} vagas encontradas\n")


    for vaga in vagas:

        print("----------------------------")
        print("Título:", vaga.get("title"))
        print("Empresa:", vaga.get("company", "Não informado"))
        print("Local:", vaga.get("location", {}).get("display_name"))
        print("Link:", vaga.get("redirect_url"))

except Exception as erro:

    print("Erro:", erro)
