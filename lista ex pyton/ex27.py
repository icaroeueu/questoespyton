def exercicio_27():
    salario = float(input("Digite o salário do colaborador: R$ "))
    if salario <= 280:
        perc = 20
    elif salario <= 700:
        perc = 15
    elif salario <= 1500:
        perc = 10
    else:
        perc = 5
    aumento = salario * perc / 100
    novo_salario = salario + aumento
    print(f"Salário antes do reajuste: R$ {salario:.2f}")
    print(f"Percentual de aumento aplicado: {perc}%")
    print(f"Valor do aumento: R$ {aumento:.2f}")
    print(f"Novo salário: R$ {novo_salario:.2f}")

if __name__ == "__main__":
    exercicio_27()
