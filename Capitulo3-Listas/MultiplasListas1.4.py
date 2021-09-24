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

#Resposta da situação 1
depreciacao=input("Digite o nome do equipamento que será depreciado: ")
for indice in range(0,len(equipamentos)):
    if depreciacao==equipamentos[indice]:
        print("Valor antigo:", valores[indice])
        valores[indice] = valores[indice] *0.9
        print("Novo valor.:", valores[indice])

#Resposta da situação 2
serial=int(input("Digite o serial do equipamento que será excluido: "))
for elemento in range(0,len(departamentos)):
    if seriais[indice]==serial:
        del departamentos[indice]
        del equipamentos[indice]
        del seriais[indice]
        del valores[indice]
        break

for indice in range(0,len(equipamentos)):
    print("Equipamento..:", (indice+1))
    print("Valor........:", equipamentos[indice])
    print("Serial.......:", seriais[indice])
    print("Departamento.:", departamentos[indice])