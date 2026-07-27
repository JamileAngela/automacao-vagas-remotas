from perfis import PERFIS


def classificar_vaga(vaga):

    texto = (
        vaga.get("titulo", "") +
        " " +
        vaga.get("descricao", "")
    ).lower()


    resultados = []


    for perfil, grupos in PERFIS.items():

        pontos = 0


        for palavra in grupos["alto"]:
            if palavra.lower() in texto:
                pontos += 3


        for palavra in grupos["medio"]:
            if palavra.lower() in texto:
                pontos += 2


        for palavra in grupos["baixo"]:
            if palavra.lower() in texto:
                pontos += 1


        if pontos > 0:
            resultados.append({
                "perfil": perfil,
                "pontuacao": pontos
            })


    return sorted(
        resultados,
        key=lambda x: x["pontuacao"],
        reverse=True
    )
