inventario=[] #comando para criação de uma lista.
resposta="S" #comando para gravar o conteúdo S na variável "resposta".
while resposta=="S": #comando para repetição, enquanto a resposta for "S" ou seja a condição for verdadeira, o comando_
    #irá se repetir.
    equipamento=[input("Equipamento: "), float(input("Valor: ")), int(input("Número Serial: ")), input("Departamento: ")]
    #criação da lista "equipamento".
    inventario.append(equipamento) #pedido para que a lista equipamento, seja inserida dentro da lista inventário.
    resposta=input("Digite S para continuar: ").upper() #solitiação de informação para que se posso definir se a_
    #condição de repetição deve continuar.

#Código para demonstrar na tela o conteúdo de uma lista
for elemento in inventario: #para cada "elemento" (variável criada no comando for) na lista "inventário" apresente.
    print("Nome.........:", elemento[0])
    print("Valor........:", elemento[1])
    print("Serial.......:", elemento[2])
    print("Departamento.:", elemento[3])

#Código para realizar busca na lista.
busca=input("Digite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
    if busca==elemento[0]: #se a variável "busca" for igual o dado constante no "elemento" da lista inventário_
        #na posição "zero"
        print("Valor..:", elemento[1])
        print("Serial.:", elemento[2])

#Código para realizar repreciação na lista.
depreciacao=input("Digite o nome do equipamento que será depreciado: ")
for elemento in inventario:
    if depreciacao == elemento[0]:
        print("Valor antigo:", elemento[1])
        elemento[1]=elemento[1]*0.9 #esta comando faz com que subscreva a informação que estava anteriormente na lista
        print("Novo valor: ", elemento[1])

#Código para identificar e excluir da lista um equipamento identificando pelo número do serial
serial=int(input("Digite o serial do equipamento que será excluído: "))
for elemento in inventario:
    if elemento[2]==serial:
        inventario.remove(elemento)

for elemento in inventario:
    print("Nome.........:", elemento[0])
    print("Valor........:", elemento[1])
    print("Serial.......:", elemento[2])
    print("Departamento.:", elemento[3])

#funções para listas numéricas
valores=[]
for elemento in inventario:
    valores.append(elemento[1])
if len(valores)>0:
    print("O equipamento mais caro custo: ", max(valores))
    print("O equipamento mais barato custo: ", min(valores))
    print("O total de equipamento é de: ", sum(valores))