import sqlite3

class Personagem:
    def __init__(self, nome, raca, classe, nivel, habilidades):
        self.nome = nome
        self.raca = raca
        self.classe = classe
        self.nivel = nivel
        self.habilidades = habilidades

    def exibir_ficha(self):
        print("Ficha do Personagem")
        print(f"Nome: {self.nome}")
        print(f"Raça: {self.raca}")
        print(f"Classe: {self.classe}")
        print(f"Nível: {self.nivel}")
        print(f"Habilidades: {', '.join(self.habilidades)}")

def criar_personagem():
    nome = input("Digite o nome do seu personagem: ")
    raca = input("Escolha a raça do seu personagem: ")
    classe = input("Escolha a classe do seu personagem: ")
    nivel = 1   # Por padrão, um personagem começa no nível 1
    habilidades = input("Digite as habilidades do personagem (separadas por vírgula): ").split(",")

    personagem = Personagem(nome, raca, classe, nivel, habilidades)
    return personagem

def salvar_personagem(personagem):
    conn = sqlite3.connect('personagens.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS personagens 
                      (nome TEXT, raca TEXT, classe TEXT, nivel INTEGER, habilidades TEXT)''')

    cursor.execute("INSERT INTO personagens VALUES (?, ?, ?, ?, ?)",
                   (personagem.nome, personagem.raca, personagem.classe, personagem.nivel, ', '.join(personagem.habilidades)))

    conn.commit()
    conn.close()

def consultar_personagens():
    conn = sqlite3.connect('personagens.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM personagens")
    personagens = cursor.fetchall()

    for personagem in personagens:
        nome, raca, classe, nivel, habilidades = personagem
        personagem = Personagem(nome, raca, classe, nivel, habilidades.split(', '))
        personagem.exibir_ficha()
    
    conn.close()

def main():
    print("Bem-vindo à criação de personagens para o RPG!")
    while True:
        opcao = input("Escolha uma opção:\n1. Criar personagem\n2. Consultar personagens\n3. Sair\n")

        if opcao == '1':
            personagem = criar_personagem()
            salvar_personagem(personagem)
        elif opcao == '2':
            consultar_personagens()
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
