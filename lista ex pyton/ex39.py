def exercicio_39():
    n1 = float(input("Digite o 1º número: "))
    n2 = float(input("Digite o 2º número: "))
    print("Operações: adição (+), subtração (-), multiplicação (*), divisão (/), exponenciação (**)")
    op = input("Escolha a operação: ")
    if op == '+':
        res = n1 + n2
    elif op == '-':
        res = n1 - n2
    elif op == '*':
        res = n1 * n2
    elif op == '/':
        if n2 == 0:
            print("Divisão por zero não permitida.")
            return
        res = n1 / n2
    elif op == '**':
        res = n1 ** n2
    else:
        print("Operação inválida.")
        return

    print(f"Resultado: {res}")

    if isinstance(res, float) and not res.is_integer():
        print("Resultado é decimal.")
    else:
        if int(res) % 2 == 0:
            print("Resultado é par.")
        else:
            print("Resultado é ímpar.")

    if res > 0:
        print("Resultado é positivo.")
    elif res < 0:
        print("Resultado é negativo.")
    else:
        print("Resultado é zero.")

    if isinstance(res, float) and res.is_integer():
        print("Resultado é inteiro.")
    elif isinstance(res, int):
        print("Resultado é inteiro.")
    else:
        print("Resultado é decimal.")

if __name__ == "__main__":
    exercicio_39()
