def exercicio_40():
    perguntas = [
        "Telefonou para a vítima? (S/N) ",
        "Esteve no local do crime? (S/N) ",
        "Mora perto da vítima? (S/N) ",
        "Devia para a vítima? (S/N) ",
        "Já trabalhou com a vítima? (S/N) "
    ]
    respostas = 0
    for p in perguntas:
        r = input(p).strip().upper()
        if r == 'S':
            respostas += 1

    if respostas == 2:
        print("Suspeita")
    elif 3 <= respostas <= 4:
        print("Cúmplice")
    elif respostas == 5:
        print("Assassino")
    else:
        print("Inocente")

if __name__ == "__main__":
    exercicio_40()
