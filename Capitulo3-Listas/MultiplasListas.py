equipamentos = []
valores = []
seriais = []
departamento = []
resposta = "S"
while resposta =="S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamento.append(input("Departamento: "))
    resposta=input("Digite S para continuar: ").upper()

for equipamento in equipamentos
    print("Equipamento:", equipamento)