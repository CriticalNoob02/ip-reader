import requests

def geoRequest(token, ip):
    """
        Função responsável pela comunicação com o endpoit de IP;
    """
    try:
        body = requests.get(f'https://geo.ipify.org/api/v2/country,city?apiKey={token}&ipAddress={ip}')
        return body.content
    except:
        erro = 'Token Inválido ou expirado!'
        print(erro)
        return erro