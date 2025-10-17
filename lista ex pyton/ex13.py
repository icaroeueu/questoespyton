kg_pesca = float(input("Digite quantos Kilogramas foram pescados: "))
multa = kg_pesca-50
multa_rs = multa*4

if kg_pesca<=50:
    print("Tudo certo com seus peixes, que foram: ",kg_pesca,"KG")
else:
    print("Foi excedido o limite de 50KG, pois foram pescados",kg_pesca,"então terá de ser pago R$",multa_rs,"")