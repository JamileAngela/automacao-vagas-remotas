print("Robô de oportunidades iniciado!")


perfis = {

    "Logística + Operações + Atendimento": [
        "logística",
        "transportes",
        "SLA",
        "customer service",
        "atendimento",
        "suporte",
        "helpdesk",
        "operações",
        "administrativo transporte"
    ],

    "Tecnologia Inicial": [
        "Python",
        "Java",
        "programação",
        "automação",
        "API",
        "dados",
        "sistemas",
        "software",
        "suporte técnico"
    ],

    "IA + Criativo + Autônomo": [
        "inteligência artificial",
        "edição de vídeo",
        "CapCut",
        "design",
        "animação",
        "conteúdo digital"
    ]

}


oportunidades = [

    {
        "tipo": "vaga",
        "titulo": "Analista de Customer Service Logístico",
        "empresa": "Empresa Exemplo",
        "modelo": "Remoto",
        "perfil": "Logística + Operações + Atendimento",
        "link": "https://exemplo.com"
    },

    {
        "tipo": "freela",
        "titulo": "Edição de vídeos curtos com IA",
        "empresa": "Cliente Exemplo",
        "modelo": "Online",
        "perfil": "IA + Criativo + Autônomo",
        "link": "https://exemplo.com"
    }

]


print("\nPerfis cadastrados:")

for perfil in perfis:
    print("-", perfil)


print("\nOportunidades encontradas:")

for oportunidade in oportunidades:
    print("--------------------")
    print("Tipo:", oportunidade["tipo"])
    print("Título:", oportunidade["titulo"])
    print("Empresa:", oportunidade["empresa"])
    print("Modelo:", oportunidade["modelo"])
    print("Perfil:", oportunidade["perfil"])
    print("Link:", oportunidade["link"])
