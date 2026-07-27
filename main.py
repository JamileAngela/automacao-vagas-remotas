from fontes.adzuna import buscar_vagas


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



print("\nTotal encontrado:", len(todas_vagas))


for vaga in todas_vagas[:20]:

    print("----------------------------")
    print("Título:", vaga.get("title"))
    print("Empresa:", vaga.get("company", {}).get("display_name"))
    print("Link:", vaga.get("redirect_url"))
