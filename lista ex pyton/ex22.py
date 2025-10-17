num1 = float(input("Digite o numero 1: "))
num2 = float(input("Digite o numero 2: "))
num3 = float(input("Digite o numero 3: "))

if num1 > num2 and num3:
    print("O numero 1 é o maior")
elif num2 > num1 and num3:
    print("O numero 2 é o maior")
elif num3 > num1 and num2:
    print("O numero 3 é o maior")