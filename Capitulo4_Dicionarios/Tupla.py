ips={}
resp="S" # Variável criada para controle o laço de repetição
while resp=="S":
    #Preencher a CHAVE do dicionário usando o octeto dividido em duas TUPLAS.
    ips[(input("Digite os dois primeiros octetos: "),
         input("Digite os dois últimos octetos: "))]=input("Nome da máquina: ")#.upper()
    resp=input("Digite <S> para continuar: ").upper()

#Aproveitando os dados da chave no formato de tupla.
print("Exibir ip's")
for ip in ips.keys(): #"KEYS" - Retorna todas as chaves do dicionário em forma de lista.
    print(ip[0]+"."+ip[1])

print("Exibindo máquinas com o mesmo endereço (redes diferentes): ")
resp="S"
while resp=="S": # utilizamos o laço de repetição para dar condição de continuação até que o lógica seja FALSA.
    pesquisa=input("Digite os dois últimos octetos: ")
    for ip,nome in ips.items(): # utilizamos o laço de repetição para situações que tem um fim após leitura de toda a base
        #print("Máquina no mesmo endereço (redes diferentes)")
        if (ip[1]==pesquisa):
            print(nome, "O IP desta máquina é "+ip[0]+"."+ip[1])
    resp=input("Digite \"S\" para realizar nova pesquisa: ").upper()

print("Exibindo as máquinas que compõem uma mesma rede:")
rede=input("Digite os dois primeiros octetos: ")
for ip,nome in ips.items():
    if (ip[0]==rede):
        print(nome, "O IP desta máquina é "+ip[0]+"."+ip[1])