from services.formatters import bytes2dict, selectMethods, splitItens
from services.paths import pathCounter, readerFile, writeFile
from services.request import geoRequest
from flask import Flask, request, jsonify

TOKEN = 'at_JfPKEM1CaGSu3uKsrGAa1CQytwghP'

def refineLoop():
    paths = pathCounter()
    totalItens = []

    for path in paths:
        file = readerFile(path)
        postFile = selectMethods(file ,"POST")
        repeatedIp, rest = splitItens(postFile, '- -')
        ips = set(repeatedIp)

        for ip in ips:
            totalItens.append(ip)

    itens = set(totalItens)
    return itens

# itens = refineLoop()
# count = 0
# for ip in itens:
#     dataBytes = geoRequest(TOKEN, ip)
#     data = bytes2dict(dataBytes)
#     writeFile(count, data)
#     count += 1

app = Flask(__name__)

@app.route('/ip/<token>', methods=['POST'])
def returnIps():
    if not request.file:
        return jsonify('Infelizmente não recebi nenhum arquivo em para ler...')  