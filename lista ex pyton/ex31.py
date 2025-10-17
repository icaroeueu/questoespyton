def exercicio_31():
    a = float(input("Digite o lado 1 do triângulo: "))
    b = float(input("Digite o lado 2 do triângulo: "))
    c = float(input("Digite o lado 3 do triângulo: "))
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            tipo = "Equilátero"
        elif a == b or b == c or a == c:
            tipo = "Isósceles"
        else:
            tipo = "Escaleno"
        print(f"Triângulo {tipo}")
    else:
        print("Os valores não formam um triângulo")

if __name__ == "__main__":
    exercicio_31()
