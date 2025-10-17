num1 = float(input("Digite o número 1: "))
num2 = float(input("Digite o número 2: "))
num3 = float(input("Digite o número 3: "))

numeros = [num1, num2, num3]

numeros.sort(reverse=True)

print("\nNúmeros em ordem decrescente:")
for num in numeros:
    print(num)