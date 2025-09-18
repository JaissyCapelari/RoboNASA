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


# Interface
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


//Restaurante 


import os

def carregar_produtos():
    produtos = {}
    if os.path.exists("produtos.txt"):
        with open("produtos.txt", "r", encoding="utf-8") as f:
            for linha in f:
                partes = linha.strip().split("|")
                if len(partes) == 3:
                    codigo = partes[0].strip()
                    nome = partes[1].strip()
                    preco = float(partes[2].strip())
                    produtos[codigo] = {"nome": nome, "preco": preco}
    return produtos

def mostrar_produtos(produtos):
    print("\n--- Produtos Disponíveis ---")
    for codigo, info in produtos.items():
        print(f"{codigo} - {info['nome']} (R$ {info['preco']:.2f})")

def obter_proximo_codigo_venda():
    if not os.path.exists("vendas.txt"):
        return 1
    with open("vendas.txt", "r", encoding="utf-8") as f:
        linhas = f.readlines()
        if linhas:
            ultimo = linhas[-1].split("|")[0].strip()
            return int(ultimo) + 1
    return 1

def salvar_venda(codigo_venda, nome_cliente, total):
    with open("vendas.txt", "a", encoding="utf-8") as f:
        f.write(f"{codigo_venda:02d}|{nome_cliente}|{total:.2f}\n")

def iniciar_comanda(produtos):
    comanda = []
    mostrar_produtos(produtos)

    while True:
        codigo = input("Digite o código do produto ou 'fim' para finalizar: ").strip()
        if codigo.lower() == "fim":
            break
        if codigo in produtos:
            comanda.append(produtos[codigo])
            print(f"{produtos[codigo]['nome']} adicionado à comanda.")
        else:
            print("Código inválido.")

    if comanda:
        nome_cliente = input("Informe o nome do cliente: ").strip()
        total = sum(item["preco"] for item in comanda)
        codigo_venda = obter_proximo_codigo_venda()
        salvar_venda(codigo_venda, nome_cliente, total)
        print(f"Venda finalizada. Total: R$ {total:.2f}")
    else:
        print("Nenhum produto foi selecionado.")

def menu():
    produtos = carregar_produtos()
    while True:
        print("\n--- MENU ---")
        print("1. Iniciar comanda")
        print("2. Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            iniciar_comanda(produtos)
        elif opcao == "2":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()


root.mainloop()
