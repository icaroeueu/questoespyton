def exercicio_34():
    data = input("Digite uma data (dd/mm/aaaa): ")
    try:
        dia, mes, ano = map(int, data.split('/'))
        import datetime
        datetime.date(ano, mes, dia)
        print("Data válida")
    except:
        print("Data inválida")

if __name__ == "__main__":
    exercicio_34()
