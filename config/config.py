import requests


def request(endpoint, key):
    # Monta URL da API com base na regra de negócio a ser executada (endpoint) e a chave de acesso da API (key).
    url = f'https://api.hgbrasil.com/{endpoint}?key={key}&format=json'

    # Retorna a request realizada para API
    response = requests.get(url)

    # Valida se a comunicação foi bem sucedida
    if 200 <= response.status_code <= 299:
        return response
    else:
        print('Status Code: ', response.status_code)
        quit()
