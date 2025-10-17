import math
tamanho = float(input("Quantos metros quadrados devem ser pintados? "))
litros_necessarios = tamanho/3
lata = math.ceil(litros_necessarios / 18)
custo = lata*80
print("Você terá que comprar: ",lata,"latas e custará: R$",custo,"")