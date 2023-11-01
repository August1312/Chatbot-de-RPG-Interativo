import time

# Função para imprimir mensagens com atraso simulando uma conversa mais natural

def imprimir_mensagem(mensagem):
    for letra in mensagem:
        print(letra, end='', flush=True)
        time.sleep(0.092)
    print("")

# Função para tomar uma decisão do jogador

def tomar_decisao():
    imprimir_mensagem("O que você gostaria de fazer?")
    imprimir_mensagem("1. Abrir a porta à esquerda")
    imprimir_mensagem("2. Seguir pelo corredor à direita")
    escolha = input("Escolha 1 ou 2: ")
    return escolha

# Função para executar a história do RPG

def historia_rpg():
    imprimir_mensagem("Bem-vindo à aventura épica do RPG!")
    imprimir_mensagem("Você está em um castelo misterioso. Há duas portas à sua frente.")
    escolha = tomar_decisao()
    if escolha == "1":
        imprimir_mensagem("Você abre a porta à esquerda e encontra um tesouro!")
    elif escolha == "2":
        imprimir_mensagem("Você segue pelo corredor à direita e enfrenta um dragão feroz!")
    else:
        imprimir_mensagem("Escolha inválida. Tente novamente.")
        historia_rpg()


historia_rpg()
