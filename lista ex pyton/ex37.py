def exercicio_37():
    valor = int(input("Valor do saque (entre 10 e 600): R$ "))
    if valor < 10 or valor > 600:
        print("Valor inválido.")
        return
    notas = {}
    for nota in [100, 50, 10, 5, 1]:
        notas[nota], valor = divmod(valor, nota)
    for nota in [100, 50, 10, 5, 1]:
        if notas[nota] > 0:
            print(f"{notas[nota]} nota(s) de R$ {nota}")

if __name__ == "__main__":
    exercicio_37()
