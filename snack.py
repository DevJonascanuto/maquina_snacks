import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

produtos = [
    {'nome':'coca-cola' , 'preco': 5.00 , 'estoque' : 5 , 'imagem': 'coca-350.png.png'},
    {'nome' : 'batata-ruffles', 'preco': 8.00 , 'estoque' : 5, 'imagem': 'ruffles.png.png'},

]

carrinho = []

def adicionar_ao_carrinho(produto):
    if produto ['estoque'] >0:
        carrinho.append(produto)
        produto['estoque'] -= 1
        atualizar_carrinho()
    else:
        messagebox.showwarning('esgotado', f'{produto ['nome'] } esta esgotado !')


def atualizar_carrinho():
    lista_carrinho_delete(0, tk.END)
    total = 0
    for item in carrinho:
        lista_carrinho.insert(tk.END, f"{item['nome']} - R$ {item['preco']: .2f} ")
        total += item['preco']
    label_total.config(text=f"total : R$ {total:.2f}")

def finalizar_compra():
    if not carrinho:
        messagebox.showinfo('compra finalizada', f'obrigado pela compra ! /nTotal : R$ {total:.2f}')
        carrinho.clear()
        atualizar_carrinho()

# janela principal do sistema.

