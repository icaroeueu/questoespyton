tamanho = float(input("Digite o tamanho do download em megabytes::???? "))
velocidade = float(input("Digite a velocidade de um link em Mbps::???? "))

tempo_em_segundos = (tamanho * 8) / velocidade
tempo_em_minutos = tempo_em_segundos / 60

print("O tempo aproximado será de exatos: " ,tempo_em_minutos)