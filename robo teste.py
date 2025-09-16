import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# Estrutura do Robô
class Robo:
    def __init__(self, identificador, nome, energia, nivel):
        self.identificador = identificador
        self.nome = nome
        self.energia = energia
        self.nivel = nivel
        self.posicao = None

    def __str__(self):
        return f"ID: {self.identificador} | Nome: {self.nome} | Energia: {self.energia} | Nível: {self.nivel} | Posição: {self.posicao}"


robos = []
campo = [[0, 0], [0, 0]]


# Funções
def cadastrar_robo():
        if len(robos) >= 4:
            messagebox.showwarning("Aviso", "Não é possível cadastrar mais robôs (limite 4).")
        return
    
    nome = simpledialog.askstring("Cadastro", "Digite o nome do robô:")
        if not nome:
            return
    energia = simpledialog.askinteger("Cadastro", "Digite a energia do robô:", minvalue=0, maxvalue=100)
    nivel = simpledialog.askinteger("Cadastro", "Digite o nível do robô:", minvalue=1, maxvalue=10)
    
        identificador = len(robos) + 1
        novo = Robo(identificador, nome, energia, nivel)
        robos.append(novo)
        messagebox.showinfo("Sucesso", f"Robô {nome} cadastrado!")


def listar_robos():
    if not robos:
        messagebox.showwarning("Aviso", "Nenhum robô cadastrado.")
        else:
            texto = "\n".join(str(r) for r in robos)
            messagebox.showinfo("Lista de Robôs", texto)


def mostrar_campo():
    campo_texto = "\n".join(str(linha) for linha in campo)
    messagebox.showinfo("Campo de Missão", campo_texto)


def simular_missao():
    if not robos:
        messagebox.showwarning("Aviso", "Nenhum robô disponível para missão.")
            return
    
    ids = [str(r.identificador) for r in robos]
    escolha = simpledialog.askstring("Missão", f"Escolha o ID do robô: {', '.join(ids)}")
    if not escolha or not escolha.isdigit():
        return

    robo = next((r for r in robos if r.identificador == int(escolha)), None)
    if not robo:
        messagebox.showwarning("Aviso", "Robô não encontrado.")
        return

    if robo.energia > 20:
        robo.energia -= 20
        while True:
            x, y = random.randint(0, 1), random.randint(0, 1)
            if campo[x][y] == 0:
                campo[x][y] = robo.identificador
                robo.posicao = (x, y)
                break
        messagebox.showinfo("Missão", f"Robô {robo.nome} entrou em missão!\nEnergia restante: {robo.energia}")
    else:
        messagebox.showwarning("Falha", f"Robô {robo.nome} não tem energia suficiente.")


def recuperar_robo():
    if not robos:
        messagebox.showwarning("Aviso", "Nenhum robô para recuperar.")
            return
    
    ids = [str(r.identificador) for r in robos if r.posicao]
    if not ids:
        messagebox.showwarning("Aviso", "Nenhum robô no campo.")
            return

    escolha = simpledialog.askstring("Recuperar", f"Escolha o ID do robô: {', '.join(ids)}")
    if not escolha or not escolha.isdigit():
            return

    robo = next((r for r in robos if r.identificador == int(escolha)), None)
    if not robo or not robo.posicao:
        messagebox.showwarning("Aviso", "Robô não encontrado no campo.")
            return

    x, y = robo.posicao
    campo[x][y] = 0
    robo.posicao = None
    messagebox.showinfo("Recuperar", f"Robô {robo.nome} foi recuperado para a base.")



root = tk.Tk()
root.title("Gerenciamento de Robôs Inteligentes")
root.geometry("400x350")

titulo = tk.Label(root, text="Agência Espacial - NASA UCDB", font=("Arial", 12, "bold"))
titulo.pack(pady=10)

btn1 = tk.Button(root, text="Cadastrar robô", width=30, command=cadastrar_robo)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Listar robôs", width=30, command=listar_robos)
btn2.pack(pady=5)

btn3 = tk.Button(root, text="Simular missão", width=30, command=simular_missao)
btn3.pack(pady=5)

btn4 = tk.Button(root, text="Mostrar campo de missão", width=30, command=mostrar_campo)
btn4.pack(pady=5)

btn5 = tk.Button(root, text="Recuperar robô", width=30, command=recuperar_robo)
btn5.pack(pady=5)

btn6 = tk.Button(root, text="Sair", width=30, command=root.quit)
btn6.pack(pady=20)

root.mainloop()
