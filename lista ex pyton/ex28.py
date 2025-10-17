def exercicio_28():
    valor_hora = float(input("Valor da hora trabalhada: R$ "))
    horas = float(input("Quantidade de horas trabalhadas no mês: "))
    salario_bruto = valor_hora * horas
    # Desconto IR
    if salario_bruto <= 900:
        ir = 0
    elif salario_bruto <= 1500:
        ir = salario_bruto * 0.05
    elif salario_bruto <= 2500:
        ir = salario_bruto * 0.10
    else:
        ir = salario_bruto * 0.20
    inss = salario_bruto * 0.10
    sindicato = salario_bruto * 0.03
    fgts = salario_bruto * 0.11
    total_descontos = ir + inss + sindicato
    salario_liquido = salario_bruto - total_descontos

    print(f"Salário Bruto: ({valor_hora} * {horas}) : R$ {salario_bruto:.2f}")
    print(f"(-) IR ({(ir/salario_bruto)*100:.0f}%) : R$ {ir:.2f}")
    print(f"(-) INSS (10%) : R$ {inss:.2f}")
    print(f"(-) Sindicato (3%) : R$ {sindicato:.2f}")
    print(f"FGTS (11%) : R$ {fgts:.2f}")
    print(f"Total de descontos : R$ {total_descontos:.2f}")
    print(f"Salário Liquido : R$ {salario_liquido:.2f}")

if __name__ == "__main__":
    exercicio_28()
