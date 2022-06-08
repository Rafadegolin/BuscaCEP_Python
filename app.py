from ctypes import pydll
import PySimpleGUI as py

def tela_inicial():
    py.theme('Dark2')

    cep = [
        [py.Text('Informe um CEP válido:', font='arial 12', pad=(0, 0))],
        [py.Input(size=(20, 0), font='arial 12', pad=(0, 0), key='cep')]
    ]

    coluna1 = [
        [py.Text('Logradouro:', font='arial 12')],
        [py.Text('Bairro:', font='arial 12')],
        [py.Text('Localidade:', font='arial 12')],
        [py.Text('UF:', font='arial 12')],
        [py.Text('IBGE:', font='arial 12')],
        [py.Text('DDD:', font='arial 12')]
    ]

    coluna2 = [
        [py.Input(font='arial 12 bold', key='logradouro', size=(35, 1))],
        [py.Input(font='arial 12 bold', key='bairro', size=(30, 1))],
        [py.Input(font='arial 12 bold', key='localidade', size=(30, 1))],
        [py.Input(font='arial 12 bold', key='uf', size=(4, 1))],
        [py.Input(font='arial 12 bold', key='ibge', size=(15, 1))],
        [py.Input(font='arial 12 bold', key='ddd', size=(4, 1))]
    ]

    botoes = [
        [py.Button('Consultar', font='arial 12', size=(10, 1), pad=((0, 15), 0)),
         py.Button('Sair', font='arial 12', size=(8, 1))]
    ]

    layout = [
        [py.Text('CONSULTAR CEP', font='arial 18 bold')],
        [py.Column(cep, justification='center', element_justification='center')],
        [py.Column(coluna1, pad=((0, 20), 0)),
         py.Column(coluna2)],
        [py.Column(botoes, justification='center')]
    ]

    teleprin = py.Window('ConsultarCEP', element_padding=(0, 10), layout=layout, size=(600, 500), finalize=True)

def consulta(cep):
    import requests

    url = 'https://viacep.com.br/ws/%s/json/' % cep 
    response = requests.get(url)
    response_json = response.json()
    return response_json


tela_inicial()
while True:
    window, event, values = py.read_all_windows()

    if event == py.WIN_CLOSED:
        break
    elif event == 'Consultar':
        try:
            logradouro = consulta(values['cep'])['logradouro']
            bairro = consulta(values['cep'])['bairro']
            localidade = consulta(values['cep'])['localidade']
            uf = consulta(values['cep'])['uf']
            ibge = consulta(values['cep'])['ibge']
            ddd = consulta(values['cep'])['ddd']

            window['logradouro'].update(logradouro)
            window['bairro'].update(bairro)
            window['localidade'].update(localidade)
            window['uf'].update(uf)
            window['ibge'].update(ibge)
            window['ddd'].update(ddd)

        except:
            py.Popup('Verifique se o campo "CEP" foi preenchio corretamente\n'
                     'ou se está conectado a internet', font='arial 12', title='ERRO')
    elif event == 'Sair':
        break