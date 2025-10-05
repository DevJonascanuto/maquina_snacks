import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import os

# --- Produtos ---
produtos = [
    {'nome':'coca-cola' , 'preco': 5.00 , 'estoque' : 5 , 'imagem': 'imagens/coca-350.png.png'},
    {'nome' : 'batata-ruffles', 'preco': 8.00 , 'estoque' : 5, 'imagem': 'imagens/ruffles.png.png'},
    {'nome' : 'agua-500ml' , 'preco': 5.00 , 'estoque' : 12, 'imagem': 'imagens/agua.png'},
    {'nome' : 'amendoim-japones' , 'preco': 9.00 , 'estoque' : 10, 'imagem': 'imagens/amendoim.jpg'},
    {'nome' : 'chocolate-80g' , 'preco': 10.00, 'estoque' : 17, 'imagem': 'imagens/lacta.png'},
    

]

carrinho = []

def adicionar_ao_carrinho(produto):
    if produto['estoque'] > 0:
        carrinho.append(produto)
        produto['estoque'] -= 1
        atualizar_carrinho()
    else:
        messagebox.showwarning('Esgotado', f"{produto['nome']} está esgotado!")

def atualizar_carrinho():
    lista_carrinho.delete(0, tk.END)
    total = 0
    for item in carrinho:
        lista_carrinho.insert(tk.END, f"{item['nome']} - R$ {item['preco']:.2f}")
        total += item['preco']
    label_total.config(text=f"Total: R$ {total:.2f}")

def finalizar_compra():
    if not carrinho:
        messagebox.showinfo('Carrinho vazio', 'Adicione itens antes de finalizar!')
        return

    total = sum(item['preco'] for item in carrinho)

    # Abre uma janelinha para escolher pagamento
    janela_pagamento = tk.Toplevel(janela)
    janela_pagamento.title("Pagamento")
    tk.Label(janela_pagamento, text=f"Total da compra: R$ {total:.2f}", font=("Arial", 14)).pack(pady=10)

    def pagar_dinheiro():
        valor_inserido = simpledialog.askfloat("Pagamento em Dinheiro", "Insira o valor pago (R$):", minvalue=0.0)
        if valor_inserido is None:
            return
        if valor_inserido < total:
            messagebox.showwarning("Saldo insuficiente", f"Você inseriu R$ {valor_inserido:.2f}, mas o total é R$ {total:.2f}")
        else:
            troco = valor_inserido - total
            messagebox.showinfo("Compra Finalizada", f"Pagamento em dinheiro realizado!\nTotal: R$ {total:.2f}\nValor pago: R$ {valor_inserido:.2f}\nTroco: R$ {troco:.2f}")
            carrinho.clear()
            atualizar_carrinho()
            janela_pagamento.destroy()

    def pagar_cartao():
        messagebox.showinfo("Compra Finalizada", f"Pagamento em cartão aprovado!\nTotal: R$ {total:.2f}")
        carrinho.clear()
        atualizar_carrinho()
        janela_pagamento.destroy()

    def pagar_pix():
        messagebox.showinfo("Compra Finalizada", f"Pagamento via Pix aprovado!\nTotal: R$ {total:.2f}")
        carrinho.clear()
        atualizar_carrinho()
        janela_pagamento.destroy()

    # Botões de pagamento
    tk.Button(janela_pagamento, text="💵 Dinheiro", width=90, command=pagar_dinheiro).pack(pady=5)
    tk.Button(janela_pagamento, text="💳 Cartão", width=90, command=pagar_cartao).pack(pady=5)
    tk.Button(janela_pagamento, text="📱 Pix", width=90, command=pagar_pix).pack(pady=5)

# --- Janela Principal ---
janela = tk.Tk()
janela.title('Máquina de Snacks')
janela.geometry("1920x1080")  # aqui altera o tamanho da tela que o programa abre

frame_produtos = tk.Frame(janela)
frame_produtos.pack(pady=20)

# Exibe produtos com imagem
for produto in produtos:
    img = Image.open(produto['imagem'])
    img = img.resize((100, 100))
    foto = ImageTk.PhotoImage(img)
    produto['foto'] = foto

    frame = tk.Frame(frame_produtos, relief='raised', borderwidth=2)
    frame.pack(side='left', padx=20)

    tk.Label(frame, image=foto).pack()
    tk.Label(frame, text=produto['nome']).pack()
    tk.Label(frame, text=f"R$ {produto['preco']:.2f}").pack()
    tk.Button(frame, text='Adicionar', command=lambda p=produto: adicionar_ao_carrinho(p)).pack()

# Carrinho
frame_carrinho = tk.Frame(janela)
frame_carrinho.pack(pady=20)

tk.Label(frame_carrinho, text='Carrinho', font=('Arial', 14)).pack()
lista_carrinho = tk.Listbox(frame_carrinho, width=40, height=10)
lista_carrinho.pack()

label_total = tk.Label(janela, text='Total: R$ 0.00', font=('Arial', 16, 'bold'))
label_total.pack()

tk.Button(janela, text='Finalizar compra', command=finalizar_compra, bg='green', fg='white', font=('Arial', 14)).pack()

# Atalho para fechar
janela.bind('<Escape>', lambda e: janela.destroy()) # finaliza o aplicativo

janela.mainloop()
