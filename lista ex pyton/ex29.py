def exercicio_29():
    dia = int(input("Digite um número (1 a 7) para o dia da semana: "))
    dias_semana = {
        1: "Domingo",
        2: "Segunda",
        3: "Terça",
        4: "Quarta",
        5: "Quinta",
        6: "Sexta",
        7: "Sábado"
    }
    print(dias_semana.get(dia, "Valor Inválido"))

if __name__ == "__main__":
    exercicio_29()