import math

area = float(input("Informe o tamanho da área a ser pintada (em m²): "))

# Acrescenta 10% de folga
area_total = area * 1.1

# Calcula a quantidade total de tinta necessária em litros
litros_necessarios = area_total / 6

# Cálculo usando apenas latas de 18L
latas = math.ceil(litros_necessarios / 18)
preco_latas = latas * 80

# Cálculo usando apenas galões de 3,6L
galoes = math.ceil(litros_necessarios / 3.6)
preco_galoes = galoes * 25

# Cálculo usando combinação (misto)
latas_mistas = int(litros_necessarios // 18)
resto = litros_necessarios - (latas_mistas * 18)
galoes_mistos = math.ceil(resto / 3.6)
preco_misto = (latas_mistas * 80) + (galoes_mistos * 25)

# Exibe os resultados
print("\nOpções de compra:")
print(f"1. Apenas latas de 18L: {latas} lata(s) - Preço: R$ {preco_latas:.2f}")
print(f"2. Apenas galões de 3,6L: {galoes} galão(ões) - Preço: R$ {preco_galoes:.2f}")
print(f"3. Mistura: {latas_mistas} lata(s) e {galoes_mistos} galão(ões) - Preço: R$ {preco_misto:.2f}")