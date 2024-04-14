valor_1 = 4
valor_2 = 6



valor_4 = 50
valor_5 = 30

valor_6 = valor_4 + valor_5

# Agora vamos transformar as operações acima em uma função:

# 1. Definir uma função com def e fornecendo os parâmetros, seus tipos e o tipo do output:

def soma(valor_1_para_somar: float,valor_2_para_somar: float = 10) -> float: # Colocando o 10 depois do float, definimos que se não for fornecido nenhum valor para 2 ele sera sempre 10.
    resultado_da_soma = valor_1_para_somar * valor_2_para_somar # Aqui escrevemos o que queremos que a função realize.
    return resultado_da_soma # Aqui definimos o retorno da função

valor_3 = soma(valor_1, valor_2)
valor_6 = soma(valor_4, valor_5)
valor_7 = soma(valor_4, )

print(valor_3)
print(valor_6)
print(valor_7)