from PrimeiroProjeto.Funcoes.Funcoes_Dicionarios import *

usuarios={}
opcao=perguntar()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        inserir(usuarios) #no parâmetro "dicionario" preencher com o nome do dicionário que foi criado, neste caso "usuário".
    if opcao=="P":
        pesquisar(usuarios, input("Qual login deseja pesquisar? ").upper()) #função "input" para que o usuário digite o chave desejada
    if opcao=="E":
        excluir(usuarios, input("Qual login deseja excluir? ").upper())
    if opcao=="L":
        listar(usuarios)
    opcao=perguntar()