from json import loads;
import re

def selectMethods(itens, pattern):
    newFile = []

    for item in itens:
        havePatter = re.findall(pattern, item)

        if havePatter: newFile.append(item)
        else: pass
        
    return newFile

def splitItens(itens, spliter):
    ip = []
    rest = []
    for e in range(len(itens)):
        separators = itens[e].split(spliter)
        for i in range(len(separators)):
            if i%2: rest.append(separators[i])
            else: ip.append(separators[i])
    return ip,rest

def bytes2dict(file):
    string_data = file.decode('utf-8')
    dic_data = loads(string_data)
    return dic_data
