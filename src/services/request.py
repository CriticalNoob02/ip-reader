import requests

def geoRequest(token, ip):
    body = requests.get(f'https://geo.ipify.org/api/v2/country,city?apiKey={token}&ipAddress={ip}')
    return body.content