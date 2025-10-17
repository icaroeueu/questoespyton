def exercicio_30():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    if 9 <= media <= 10:
        conceito = 'A'
    elif 7.5 <= media < 9:
        conceito = 'B'
    elif 6 <= media < 7.5:
        conceito = 'C'
    elif 4 <= media < 6:
        conceito = 'D'
    else:
        conceito = 'E'

    status = "APROVADO" if conceito in ['A', 'B', 'C'] else "REPROVADO"

    print(f"Notas: {nota1:.1f} e {nota2:.1f}")
    print(f"Média: {media:.2f}")
    print(f"Conceito: {conceito}")
    print(status)

if __name__ == "__main__":
    exercicio_30()