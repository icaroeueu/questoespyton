def exercicio_36():
    n1 = float(input("Digite a 1ª nota: "))
    n2 = float(input("Digite a 2ª nota: "))
    n3 = float(input("Digite a 3ª nota: "))
    media = (n1 + n2 + n3) / 3
    if media == 10:
        print(f"Aprovado com Distinção! Média: {media:.2f}")
    elif media >= 7:
        print(f"Aprovado! Média: {media:.2f}")
    else:
        print(f"Reprovado! Média: {media:.2f}")

if __name__ == "__main__":
    exercicio_36()
