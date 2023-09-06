from services.paths import pathCounter, readerFile
from services.formatters import selectMethods, splitItens

def refineLoop(method:str):
    """
        Função responsável por loopar a pasta de arquivos recebidos e processar os dados
        retorna apenas  os ips que fizeram as requisições do metodo POST
    """
    paths = pathCounter()
    totalItens = []

    for path in paths:
        file = readerFile(path)
        postFile = selectMethods(file ,method)
        repeatedIp, rest = splitItens(postFile, '- -')
        ips = set(repeatedIp)

        for ip in ips:
            totalItens.append(ip)

    itens = set(totalItens)
    return itens
