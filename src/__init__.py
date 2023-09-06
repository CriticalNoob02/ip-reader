from services.formatters import bytes2dict
from services.request import geoRequest
from functions.loop import refineLoop, clearLoop
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

HOST = '0.0.0.0'
PORT = 5000

@app.route('/sendFile', methods=['POST'])
def saveFiles():
    try:
        code = uuid.uuid4()
        file = request.files['logs']

        if file is None: return jsonify({'error': 'Nenhum arquivo enviado'}), 400

        file.save(f'src/files/logs/{code}.txt')
        return jsonify({'message': 'Arquivo recebido com sucesso!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/getIP/<method>', methods=['GET'])
def getIPs(method):
    try:
        ips = refineLoop(method)
        return jsonify(list(ips)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/getInfo/<method>/<token>', methods=['GET'])
def getInfo(method, token):
    try:
        itens = refineLoop(method)
        arrayData = []
        for ip in itens:
            dataBytes = geoRequest(token, ip)
            data = bytes2dict(dataBytes)
            arrayData.append(data)
        return jsonify(arrayData), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/delete', methods=['DELETE'])
def deleteIPs():
    try:
        PATH = 'logs'
        clearLoop(PATH)
        return jsonify({f"message": "Todos os arquivos da pasta {PATH} foram deletados"}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500



app.run(host=HOST, port=PORT)