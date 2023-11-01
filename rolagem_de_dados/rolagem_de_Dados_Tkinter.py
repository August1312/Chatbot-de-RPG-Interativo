import tkinter as tk
import random

def rolar_dado():
    comando = entrada_texto.get().lower()  # Converta o comando para letras minúsculas 
    if comando.startswith("d"):
        try:
            dado = int(comando[1:])
            resultado = random.randint(1, dado)
            label_resultado.config(text=f"Resultado: {resultado}")
        except ValueError:
            label_resultado.config(text="Comando inválido. Use um número válido para 'dx'.")
    else:
        label_resultado.config(text="Comando inválido. Use o formato 'dx', onde x é o número de lados do dado.")

# Crie uma janela

janela = tk.Tk()
janela.title(" Sumário de Dados de Aventuras Épicas")
janela.geometry("400x200")


label_instrucao = tk.Label(janela, text="Digite o número de lados do dado (ex: D20):", font=("Helvetica", 12))
label_instrucao.pack(pady=10)


entrada_texto = tk.Entry(janela)
entrada_texto.pack(pady=5)


botao_rolar = tk.Button(janela, text="Rolar Dado", command=rolar_dado)
botao_rolar.pack(pady=10)

label_resultado = tk.Label(janela, text="", font=("Helvetica", 14))
label_resultado.pack()

janela.mainloop()
