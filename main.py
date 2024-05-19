import random
import PySimpleGUI as sg

def gerador_senha(numero, tamanho_da_senha):
    print("Bem vindo ao gerador de senhas")
    letras = 'abcdefghijklmnopqvxyz,-_#@%$&*.'

    print('\nAqui estão suas senhas:')
    senhas = []
    for _ in range(numero):
        senha = ''
        for _ in range(tamanho_da_senha):
            senha += random.choice(letras)
        senhas.append(senha)
    return senhas

# layout
sg.theme('Reddit')
layout = [
    [sg.Text('Numero de senhas a ser gerada:'), sg.Input(key='numero_de_senhas', size=(20, 1))],
    [sg.Text('Numero de caracteres da senha:'), sg.Input(key='tamanho', size=(20, 1))],
    [sg.Button('Gerar')],
    [sg.Text('Senhas geradas:', size=(20, 1))],
    [sg.Output(size=(50, 10))]
]

# janela
janela = sg.Window('Gerador de senhas', layout)

# leitura de eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Gerar':
        numero = int(valores['numero_de_senhas'])
        tamanho_da_senha = int(valores['tamanho'])
        senhas = gerador_senha(numero, tamanho_da_senha)
        for senha in senhas:
            print(senha)

janela.close()
