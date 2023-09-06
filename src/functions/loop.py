from services.paths import pathCounter, readerFile, deleteFile
from services.formatters import selectMethods, splitItens

def refineLoop(method:str):
    """
        Função responsável por loopar a pasta de arquivos recebidos e processar os dados
        retorna apenas  os ips que fizeram as requisições do metodo POST
    """
    paths = pathCounter(path='logs')
    totalItens = []

    for path in paths:
        file = readerFile(pathName=path)
        postFile = selectMethods(itens=file ,pattern=method)
        repeatedIp, rest = splitItens(itens=postFile, spliter='- -')
        ips = set(repeatedIp)

        for ip in ips:
            totalItens.append(ip)

    itens = set(totalItens)
    return itens

def clearLoop(path):
    """
        Função responsável por loopar e deletar todos os arquivos da pasta selecionada;
    """
    paths = pathCounter(path)
    for file in paths:
        deleteFile(file, path)
        print(f'O arquivo {file} foi excluido!')