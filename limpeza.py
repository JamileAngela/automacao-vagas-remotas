def remover_duplicadas(vagas):

    vagas_unicas = []
    links = set()

    for vaga in vagas:

        link = vaga.get("redirect_url")

        if link not in links:
            vagas_unicas.append(vaga)
            links.add(link)

    return vagas_unicas
