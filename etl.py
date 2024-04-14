import csv

path_arquivo = "vendas.csv"

def ler_csv(nome_arquivo_csv: str) -> list[dict]:
    """Função que le um arquivo csv e retorna uma lista
       de dicionários.

    Args:
        nome_arquivo_csv (str): 

    Returns:
        list[dict]:
    """
    lista = []
    with open(nome_arquivo_csv, mode="r", encoding="utf-8") as arquivo: # Aqui criamos um contexto com with, ele é responsavel por abrir e fechar e tranformamos tudo em um variável.
        leitor = csv.DictReader(arquivo) # Aqui usamos o modulo csv para ler a variável criada anteriormente.
        for linha in leitor: # Aqui estamos inteirando sobre a lista e já convertendo ela.
            lista.append(linha)
    return lista

"""vendas_itens: list[dict]

vendas_itens = ler_csv(path_arquivo) # Checando se a função está funcionando

print(vendas_itens)"""

def filtrar_produtos_não_entregues(lista: list[dict]) -> list[dict]: # o output da função anterior e o nosso input desta função
    """
    Função que filtra produtos onde entrega = True.
    
    """
    lista_com_produtos_filtrados = []
    for produto in lista:
        if produto.get("entregue") == "True": # Nesta condição estamos usando o get para fazer uma comparação.
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados


# print(produtos_entregues)

def somar_valores_produtos(lista_com_produtos_filtrados: list[dict]) -> int:
    """
    Soma todos os produtos que estão na lista.
    """
    valor_total = 0
    for produto in lista_com_produtos_filtrados:
        valor_total += int(produto.get("price"))
    return valor_total



