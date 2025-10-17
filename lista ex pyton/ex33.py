def exercicio_33():
    ano = int(input("Digite um ano: "))
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")

if __name__ == "__main__":
    exercicio_33()
