# janela - 500x500
# titulo - Conversor de Moedas
# campos de selecionar moedas de origem e destino (campos de listas) com labels
# botão de "converter"
# lista de exibição com os nomes das moedas

import customtkinter as ctkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis
from pegar_cotacao import pegar_cotacao_moeda

# criar e configurar a janela
ctkinter.set_appearance_mode("dark")
ctkinter.set_default_color_theme("dark-blue")

janela = ctkinter.CTk()
janela.geometry("500x700")

# criar os botões, textos e outros elementos                     fonte e tamanho
titulo = ctkinter.CTkLabel(janela, text="Conversor de Moedas", font=("", 26))

dic_conversoes_disponiveis = conversoes_disponiveis()

def carregar_moedas_destino(moeda_selecionada):
    lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada]
    campo_moeda_destino.configure(values=lista_moedas_destino)
    campo_moeda_destino.set(lista_moedas_destino[0])


texto_moeda_origem = ctkinter.CTkLabel(janela, text="Selecione a moeda de origem")
campo_moeda_origem = ctkinter.CTkOptionMenu(janela, values=list(dic_conversoes_disponiveis.keys()),
                                            command=carregar_moedas_destino)

texto_moeda_destino = ctkinter.CTkLabel(janela, text="Selecione a moeda de destino")
campo_moeda_destino = ctkinter.CTkOptionMenu(janela, values=["Selecione uma moeda de origem"])


def converter_moeda():
    moeda_origem = campo_moeda_origem.get()
    moeda_destino = campo_moeda_destino.get()
    if moeda_destino != 'Selecione uma moeda de origem':
        cotacao = pegar_cotacao_moeda(moeda_origem, moeda_destino)
        texto_cotacao_moeda.configure(text=f"1  {moeda_origem}  =  {cotacao}  {moeda_destino}")


botao_converter = ctkinter.CTkButton(janela, text="Converter",
                                     command=converter_moeda)

texto_cotacao_moeda = ctkinter.CTkLabel(janela, text="")


lista_moedas = ctkinter.CTkScrollableFrame(janela, width=250)

moedas_disponiveis = nomes_moedas()
for codigo_moeda in moedas_disponiveis:
    nome_moeda = moedas_disponiveis[codigo_moeda]
    texto_moeda = ctkinter.CTkLabel(lista_moedas, text=f'{codigo_moeda} - {nome_moeda}')
    texto_moeda.pack()


def pesquisar_codigos():
    texto = barra_pesquisa.get(0.0, 'end').replace('\n', '').lower()
    moedas_disponiveis = nomes_moedas()

    for texto_moeda in lista_moedas.winfo_children():
        texto_moeda.destroy()

    if texto != '':
        for moeda in moedas_disponiveis:
            if texto in moeda.lower() or texto in moedas_disponiveis[moeda].lower():
                nome_moeda = moedas_disponiveis[moeda]
                texto_moeda = ctkinter.CTkLabel(lista_moedas, text=f'{moeda} - {nome_moeda}')
                texto_moeda.pack()
    else:
        for moeda in moedas_disponiveis:
            nome_moeda = moedas_disponiveis[moeda]
            texto_moeda = ctkinter.CTkLabel(lista_moedas, text=f'{moeda} - {nome_moeda}')
            texto_moeda.pack()


texto_pesquisa = ctkinter.CTkLabel(janela, text="Pesquise as moedas disponíveis")
barra_pesquisa = ctkinter.CTkTextbox(janela, width=250, height=30)
botao_pesquisa = ctkinter.CTkButton(janela, text="Pesquisar", command=pesquisar_codigos)


# colocar todos os elementos na tela
titulo.pack(padx=10, pady=10)
texto_moeda_origem.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=10)
texto_moeda_destino.pack(padx=10, pady=10)
campo_moeda_destino.pack(padx=10)
botao_converter.pack(padx=10, pady=20)
texto_cotacao_moeda.pack(padx=10)
texto_pesquisa.pack(padx=10)
barra_pesquisa.pack(padx=10)
botao_pesquisa.pack(padx=10, pady=10)
lista_moedas.pack(padx=10, pady=10)

# rodar a janela
janela.mainloop()
