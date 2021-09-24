def preencherInventario(lista):
    resp="S"
    while resp=="S":
        equipamento=[input("Equipamnto: "),
                     float(input("Valor: ")),
                     int(input("Número Serial: ")),
                     input("Departamento: ")]
        lista.append(equipamento)
        resp=input("Digite \"S\" para continuar: ").upper()

def exibirInventario(lista):
    for elemento in lista:
        print("Nome.........:", elemento[0])
        print("Valor........:", elemento[1])
        print("Serial.......:", elemento[2])
        print("Departamento.:", elemento[3])

def localizarPorNome(lista):
    busca=input("Digite o nome do equipamento que deseja buscar: ")
    for elemento in lista:
        if busca==elemento[0]:
            print("Valor..:", elemento[1])
            print("Serial.:", elemento[2])

def depreciarPorNome(lista, porc): #pode-se declarar mais de um parâmetro na função
    depreciacao=input("Digite o nome do equipamento que será depreciado: ")
    for elemento in lista:
        if depreciacao==elemento[0]:
            print("Valor antigo:", elemento[1])
            elemento[1]=elemento[1]*(1-porc/100)
            print("Novo valor:", elemento[1])

def excluirPorSerial(lista): #esta função deve ser chamada dentro do comando print para pode ler a mensagam do retorno.
    serial=int(input("Digite o serial do equipamento que será excluído: "))
    for elemento in lista:
        if serial==elemento[2]:
            lista.remove(elemento)
    return "Itens excluídos."

def resumirValores(lista):
    valores=[]
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores)>0:
        print("O equipamento mais caro custa:", max(valores))
        print("O equipamento mais barato custa:", min(valores))
        print("O total de equipamento é de:", sum(valores))