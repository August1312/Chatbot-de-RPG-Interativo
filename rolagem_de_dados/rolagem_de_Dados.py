import random

def rolar_dado(dado):
    return random.randint(1, dado)

while True:
    comando = input("Digite um comando (ou 'sair' para encerrar): ")
    
    if comando.lower() == 'sair':
        break
    
    if comando.startswith("d"):
        try:
            dado = int(comando[1:])
            resultado = rolar_dado(dado)
            print(f"Você rolou um D{dado} e obteve o resultado: {resultado}")
        except ValueError:
            print("Comando inválido. Use o formato 'dX', onde X é o número de faces do dado.")
    else:
        print("Comando inválido. Use o formato 'dX', onde X é o número de faces do dado.")
