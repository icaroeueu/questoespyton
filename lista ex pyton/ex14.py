hora = float(input("Quanto você ganha por hora? "))
hrs_trab = float(input("Quantas horas você trabalha no mês? "))
salario_bruto = hora*hrs_trab
ir = salario_bruto*0.11
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05
salario_liq = salario_bruto-ir-inss-sindicato

print("Seu salário bruto é de: R$",salario_bruto)
print("O valor descontado pelo Imposto de renda de seu salário é de: R$ {:.1f}".format(ir))
print("O valor descontado pelo INSS de seu salário é de: R$ {:.1f}".format(inss))
print("O valor descontado pelo Sindicato de seu salário é de: R$ {:.1f}".format(sindicato))
print("Seu salário líquido é de: R$",salario_liq)