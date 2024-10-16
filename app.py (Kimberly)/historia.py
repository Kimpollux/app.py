import random

# Função que gera a introdução da história
def gerar_introducao():
    introducoes = ["Em um belo dia", "Em um dia chuvoso", "Alguns anos atrás"]
    return random.choice(introducoes)

# Função que gera o desenvolvimento da história
def gerar_desenvolvimento():
    desenvolvimentos = ["uma garota curiosa", "um caçador destemido", "uma mulher corajosa",
                        "um garoto atrapalhado", "uma exploradora determinada"]
    return random.choice(desenvolvimentos)

# Função que gera o final da história
def gerar_final():
    finais = ["caiu em uma caverna secreta,", "descobriu uma ilha perdida.",
              "resgatou sua amiga de uma montanha.", "descobriu uma nova espécie marinha.",
              "desvendou um segredo histórico.", "visitou uma floresta assombrada."]
    return random.choice(finais)

# Função principal que gera toda a história
def gerar_historia():
    introducao = gerar_introducao()
    desenvolvimento = gerar_desenvolvimento()
    final = gerar_final()

    historia = f"{introducao} {desenvolvimento} {final}"
    return historia

# Exibe a história gerada
if __name__ == "__main__":
    print(gerar_historia())