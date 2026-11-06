import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("600x800")

def digitar(numero):
    visor.insert(tk.END, numero)
    
def limpar():
    visor.delete(0, tk.END)

def apagar():
    conteudo= visor.get()
    visor.delete(0, tk.END)
    visor.insert(0, conteudo[:-1])

def somar():
    soma


def digitar_menos():
    visor.insert(tk.END,"9")

def digitar_multiplicação():
    visor.insert(tk.END,"9")



visor = tk.Entry(janela, width=24, justify="right", font=("Arial", 12))
visor.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

botao_C = tk.Button(
    janela,
    text="C",
    width=6, height=2,
    command=limpar    
)
botao_C.grid(row=1, column=0, padx=2, pady=2)

botao_apagar = tk.Button(
    janela,
    text="⌫",
    width=6, height=2,
    command=apagar
)
botao_apagar.grid(row=1, column=1, padx=2, pady=2)

botao_divisao = tk.Button(janela, text="÷", width=6, height=2)
botao_divisao.grid(row=1, column=2, padx=2, pady=2)

botao_mult = tk.Button(janela, text="x", width=6, height=2)
botao_mult.grid(row=1, column=3, padx=2, pady=2)

botao_7 = tk.Button(
    janela, 
    text="7", 
    width=6, height=2,
    command=lambda: digitar("7")
)
botao_7.grid(row=2, column=0, padx=2, pady=2)

botao_8 = tk.Button(
    janela, 
    text="8", 
    width=6, height=2,
    command=lambda: digitar("8")
)
botao_8.grid(row=2, column=1, padx=2, pady=2)

botao_9 = tk.Button(
    janela, 
    text="9", 
    width=6, height=2,
    command=lambda: digitar("9")
)
botao_9.grid(row=2, column=2, padx=2, pady=2)

botao_menos = tk.Button(janela, text="-", width=6, height=2)
botao_menos.grid(row=2, column=3, padx=2, pady=2)

botao_4 = tk.Button(
    janela, 
    text="4", 
    width=6, height=2,
    command=lambda: digitar("4")
)
botao_4.grid(row=3, column=0, padx=2, pady=2)

botao_5 = tk.Button(
    janela, 
    text="5", 
    width=6, height=2,
    command=lambda: digitar("5")
)
botao_5.grid(row=3, column=1, padx=2, pady=2)

botao_6 = tk.Button(
    janela, 
    text="6", 
    width=6, height=2,
    command=lambda: digitar("6")
)
botao_6.grid(row=3, column=2, padx=2, pady=2)

botao_soma = tk.Button(janela, text="+", width=6, height=2)
botao_soma.grid(row=3, column=3, padx=2, pady=2)

botao_1 = tk.Button(
    janela, 
    text="1", 
    width=6, height=2,
    command=lambda: digitar("1")
)
botao_1.grid(row=4, column=0, padx=2, pady=2)

botao_2 = tk.Button(
    janela, 
    text="2", 
    width=6, height=2,
    command=lambda: digitar("2")
)
botao_2.grid(row=4, column=1, padx=2, pady=2)

botao_3 = tk.Button(
    janela, 
    text="3", 
    width=6, height=2,
    command=lambda: digitar("3")
)
botao_3.grid(row=4, column=2, padx=2, pady=2)

botao_igual = tk.Button(janela, text="=", width=6, height=5)
botao_igual.grid(row=4, column=3, rowspan=2, padx=2, pady=2)

botao_0 = tk.Button(
    janela, 
    text="0", 
    width=14, height=2,
    command=lambda: digitar("0")
    )
botao_0.grid(row=5, column=0, columnspan=2, padx=2, pady=2)

botao_ponto = tk.Button(janela, text=".", width=6, height=2)
botao_ponto.grid(row=5, column=2, padx=2, pady=2)




janela.mainloop()