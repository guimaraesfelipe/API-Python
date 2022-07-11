import PySimpleGUI as sg
from modules.finance import quotations

# Gera uma lista dinamicamente das moedas cadastradas na API
list_coins = list(dict.keys(quotations.response.json()['results']['currencies']))
# Remove o indice 0 da lista de moedas, correspondente ao SOURCE == BRL (Valor de retorno)
list_coins.pop(0)

# Leyout == Elementos da interface gráfica em modo de lista Python
layout = [
    [sg.Text('Qual moeda deseja verificar a cotação atual? '), sg.Combo(list_coins, size=(10, 10), key='coin')],
    [sg.Button('Consultar Valor', size=(12, 1))],
    [sg.Text('', key='return')]
]

# Instanciando a janela com seu NOME e LAYOUT
window = sg.Window('Cotação de Moedas', layout)

# Loop infinito para garantir a execução da aplicação equanto o fluxo não for concluído
while True:
    # Retorna o EVENTOS e VALORES após interação do usuário com a janela
    events, values = window.read()

    # Se o EVENTOS for o método WINDOW_CLOSED (Fechar janela via botão X ou qualquer outra forma de execução do método)
    if events == sg.WINDOW_CLOSED:
        # Sai do loop infinito e encerra o programa
        break

    # Se EVENTOS for o acionamento do botão CONSULTAR VALOR
    if events == 'Consultar Valor':
        # Retorna valores da API conforme o arquivo quotations.py
        api = quotations.response

        # Filtra o caminho dentro do .json até os dados das moédas
        path = api.json()['results']['currencies'][values['coin']]

        # Sobescreve o elemento return do leyout da janela com os valores da méda selecionada
        window.Element('return').update(f'{path["name"]}: R$ {path["buy"]}')
