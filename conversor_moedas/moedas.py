import requests

def get_cotacao(moeda_destino = 'BRL'):
    url = f"https://api.exchangerate-api.com/v4/latest/{moeda_destino}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Erro ao obter a cotação")
        return None

    data = response.json()
    return data["rates"]


def converter_cotacao(moeda_origem = 'USD', moeda_destino = 'BRL', valor = 1):
    rates = get_cotacao(moeda_destino)
    return round((valor / rates[moeda_origem]), 4) 
