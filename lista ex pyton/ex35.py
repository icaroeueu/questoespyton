def exercicio_35():
    n = int(input("Digite um número inteiro menor que 1000: "))
    if not (0 <= n < 1000):
        print("Número inválido.")
        return
    centenas = n // 100
    dezenas = (n % 100) // 10
    unidades = n % 10

    partes = []
    if centenas > 0:
        partes.append(f"{centenas} {'centena' if centenas == 1 else 'centenas'}")
    if dezenas > 0:
        partes.append(f"{dezenas} {'dezena' if dezenas == 1 else 'dezenas'}")
    if unidades > 0 or n == 0:
        partes.append(f"{unidades} {'unidade' if unidades == 1 else 'unidades'}")

    if len(partes) > 1:
        texto = ", ".join(partes[:-1]) + " e " + partes[-1]
    else:
        texto = partes[0]

    print(f"{n} = {texto}")

if __name__ == "__main__":
    exercicio_35()
