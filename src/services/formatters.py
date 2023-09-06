from json import loads;
import re
import numpy

def selectMethods(itens, pattern):
    """
        Função responsável por realizar a separação de metodos de request do log;
    """
    newFile = []

    for item in itens:
        havePatter = re.findall(pattern, item)

        if havePatter: newFile.append(item)
        else: pass
        
    return newFile

def splitItens(itens, spliter):
    """
        Função responsável por realizar a unificação de ips devolvendo apenas ips diferentes; 
    """
    ip = []
    rest = []
    for e in range(len(itens)):
        separators = itens[e].split(spliter)
        for i in range(len(separators)):
            if i%2: rest.append(separators[i])
            else: ip.append(separators[i])
    return ip,rest

def bytes2dict(file):
    """
        Função responsável por transformar dados do formato bytes em dict
    """
    string_data = file.decode('utf-8')
    dic_data = loads(string_data)
    return dic_data

def bytes2array(file):
    """
        Função responsável transformar os dados bytes em array;
    """
    string_data = file.decode('utf-8')
    dic_data = loads(string_data)
    array_dic = numpy.array(dic_data)
    return array_dic
