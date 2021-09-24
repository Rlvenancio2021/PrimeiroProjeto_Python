equipamentos=[]
valores=[]
seriais=[]
departamentos=[]
resposta="S"
while resposta=="S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta=input("Digite S para continuar: ").upper()

for indice in range(0,len(equipamentos)):
    print("Equipamento..:",(indice+1))
    print("Nome.........: ",equipamentos[indice])
    print("Valor........: ",valores[indice])
    print("Serial.......: ",seriais[indice])
    print("Departamento.: ",departamentos[indice])
#Para a variável "indice"que criamos no "for", será atribuído o valor de 0 até a quantidade de elementos_
#que existirem dentro da nossa lista "equipamentos" (função "len()").

#Código para realizar busca dentro do indice
busca=input("Digite o nome do equipamento que deseja buscar: ")
for indice in range(0,len(equipamentos)):
    if busca==equipamentos[indice]:
        print("Valor..:", valores[indice])
        print("Serial.:", seriais[indice])