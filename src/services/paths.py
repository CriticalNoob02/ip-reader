import os
from json import dump

def pathCounter(path:str):
    """
        Função responsável por coletar todos os arquivos dentro da pasta de arquivos da sua escolha;
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

def deleteFile(pathName:str,path:str):
    """
        Função resposável por limpar o cache de dados recebidos;
        @param - `pathName` nome do arquivo
        @param - `path` diretório do arquivo
    """
    dir = f"src/files/{path}"
    os.remove(os.path.join(dir, pathName))
