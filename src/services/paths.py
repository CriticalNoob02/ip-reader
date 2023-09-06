import os
from json import dump

def pathCounter(path:str):
    """
        função responsável por coletar todos os arquivos dentro da pasta de arquivos da sua escolha;
    """
    paths = []
    dir = f"src/files/{path}"
    for path in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, path)):
            paths.append(path)
    return paths

def readerFile(pathName):
    """
        Função responsável por realiza a leitura dos arquivos selecionados;
    """
    arquivo = open(f'src/files/logs/{pathName}')
    leitura = arquivo.readlines()
    
    return leitura

def writeFile(name, data):
    """
        Função responsável por escrever arquivos no formato JSON;
    """
    with open(f"src/files/ips/ip_{name}.json", "w") as file:
        dump(data, file)
