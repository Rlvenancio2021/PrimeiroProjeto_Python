from PrimeiroProjeto.Funcoes.Funcoes_Arquivos import *

inventario={}
opcao=chamarMenu()

while opcao>0 and opcao<4:
    if opcao==1:
        registrar(inventario)
    elif opcao==2:
        persistir(inventario)
    elif opcao==3:
        resultado=exibir()
        for linha in resultado:
            print(linha[linha.find(";")+1:-1]) # Encontra o primero ";" e apresenta o conteúdo a partir dele,
            #considerando iniciando na posição zero.

            lista=linha.split(";") # quebra o arquivo a cada ";" encontrado.
            print("Data.........:", lista[1]) # consideradndo que patrimonio esta na posição zero.
            print("Descrição....:", lista[2])
            print("Departamento.:", lista[3])
    opcao=chamarMenu()