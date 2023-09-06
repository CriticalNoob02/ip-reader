from services.formatters import bytes2dict
from services.request import geoRequest
from functions.loop import refineLoop
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

@app.route('/sendFile', methods=['POST'])
def saveFiles():
    if not request.file: return jsonify('Infelizmente não recebi nenhum arquivo em para ler...')
    else:
        code = uuid.uuid4()
        file = request.files['logs']    
        file.save(f'src/files/logs/{code}.txt')
        return jsonify('Arquivo recebido com sucesso!')

@app.route('/getIps', methods=['GET'])
def getIps():
    ips = refineLoop()
    return jsonify(list(ips))

@app.route('/getInfo/<token>', methods=['GET'])
def getInfo(token):
    itens = refineLoop()
    arrayData = []
    for ip in itens:
        dataBytes = geoRequest(token, ip)
        data = bytes2dict(dataBytes)
        arrayData.append(data)
    return jsonify(arrayData)


app.run(port=5000, debug=True)