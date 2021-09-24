#DEFINIR FUNÇÃO DE PERGUNTA
def perguntar():
    resposta=input("O que deseja realizar? "
                   "\n <I> - Para Inserir um usuário "
                   "\n <P> - Para Pesquisar um usuário "
                   "\n <E> - Para Excluir um usuário "
                   "\n <L> - Para Listar um ususário "
                   "\n Digite sua opção: ").upper()
    return resposta

#DEFINIR FUNÇÃO DE CRIAR O DICIONÁRIO PARA INSERIR OS DADOS
def inserir(dicionario):
    chave=input("Digeite o login: ").upper()
    dicionario[chave]=[input("Digite o nome: ").upper(),
                       input("Digite a última data de acesso: "),
                       input("Qual a última estação acessada: ").upper()]

#DEFINIR FUNÇÃO DE PESQUISA NO DICIONÁRIO
def pesquisar(dicionario, chave):#"dicionario" (onde ser pretende pesquisar); "chave" (o dado que será pesquisado).
    lista=dicionario.get(chave) #Criar a variável lista, com os dados obtidos da função .get().
    if lista!=None: #"None" palavra reservada do Python indica vazio
        print("Nome...........: " + lista[0])
        print("Último acesso..: " + lista[1])
        print("Última estação.: " + lista[2])

#DEFINIR FUNÇÃO DE EXCLUIR NO DICIONÁRIO
def excluir(dicionario,chave): # É uma forma de executar um "foreach" (para cada)
    if dicionario.get(chave)!=None:
        del dicionario[chave]
    print("Objeto Eliminado")

#DEFINIR FUNÇÃO DE LISTAR NO DICIONÁRIO
def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto.......")
        print("Login: ", chave)
        print("Dados: ", valor)