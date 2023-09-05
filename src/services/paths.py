import os
from json import dump

def pathCounter():
    paths = []
    dir = "src/files/logs"
    for path in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, path)):
            paths.append(path)
    return paths

def readerFile(pathName):
    arquivo = open(f'src/files/logs/{pathName}')
    leitura = arquivo.readlines()
    
    return leitura

def writeFile(name, data):
        with open(f"src/files/ips/ip_{name}.json", "w") as file:
            dump(data, file)
