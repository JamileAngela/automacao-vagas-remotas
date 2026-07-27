from perfis import PERFIS


def classificar_vaga(vaga):

    texto = (
        vaga.get("titulo", "") +
        " " +
        vaga.get("descricao", "")
    ).lower()

    resultados = []

    for perfil, palavras in PERFIS.items():

        pontos = 0

        for palavra in palavras:
            if palavra.lower() in texto:
                pontos += 1

        if pontos > 0:
            resultados.append({
                "perfil": perfil,
                "pontuacao": pontos
            })

    return resultados
