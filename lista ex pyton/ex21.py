nota1 = int(input("Digite a nota 1: "))
nota2 = int(input("Digite a nota 2: "))
media = (nota1+nota2)/2

if media==10:
    print("Aprovado com Distinção")
elif media>=7:
    print("Aprovado")
elif media<7:
    print("Reprovado")