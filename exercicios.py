from typing import List
import statistics as sts

# 1. Calcular Média de Valores em uma Lista:

# lista: list[int] = [1,2,3,4,5,6,7,8,9,10]

# def media_valores_lista(lista: List[int]) -> float:
#     resultado_media = sum(lista) / len(lista)
#     return resultado_media

# lista_media = media_valores_lista(lista)

# print(lista_media)

# 2. Filtrar Dados Acima de um Limite

# lista: list[int] = [1,2,3,4,5,6,7,8,9,10]
# limite = 5

# def filtrar_dados(lista: List[int]) -> int:
#     lista_nova = []
#     for n in lista:
#         if n > limite:
#             lista_nova.append(n)
#     return lista_nova
# nova_lista = filtrar_dados(lista)

# print(nova_lista)

# 3. Contar Valores Únicos em uma Lista

# valores: List[int] = [1,1,4,6,6,8,10,8,9,9,7]

# def contar_valores_unicos(valores: List[int]) -> int:
#     resultado = len(set(valores))
#     return resultado

# print(contar_valores_unicos(valores))

# 4.Converter Celsius para Fahrenheit em uma Lista

# t_c: float = float(input("Coloque a temperatura em Celsius: "))


# def c_para_f(t_c: float) -> float:
#     t_f = (t_c * 1.8) + 32
#     return t_f

# print(f"A temperatura {t_c} em celsius é igual à {c_para_f(t_c)} em Fahrenheit")

# 5. Calcular Desvio Padrão de uma Lista

# valores: List[float] = [1,1,4,6,6,8,10,8,9,9,7]

# def desvio_padrao(valores: List[float]) -> float:
#     resultado = sts.stdev(valores)
#     return resultado

# print(f"O Desvio Padrão dos elementos da lista {valores} é {desvio_padrao(valores):.2f} ")

# 6. Encontrar Valores Ausentes em uma Sequência

# sequencia: List[int] = [1,2,4,5,7,8,9,11]

# def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
#     completo = set(range(min(sequencia), max(sequencia) + 1))
#     return list(completo - set(sequencia))
# print(F"Números faltantes da lista {sequencia} são: {encontrar_valores_ausentes(sequencia)}")