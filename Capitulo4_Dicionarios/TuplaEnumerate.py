usuario={}
resp="S" #para controlar o laço de repetição.
emails=[]
while resp=="S":
    emails.append(input("Digite um e-mail: ").lower())
    resp=input("Digite \"S\" para continuar: ").upper()

tupla=list(enumerate(emails)) #Gerando uma tupla com cada elemento (usando a função "list").
for chave in range(0,len(tupla)): #Enumerando cada item encontrado na lista "emails";
                                  # Função "range" controla o laço "for" de zera até a quantidade de elementos encontrados na TUPLA.
    print("Email: ", tupla[chave][1]) # Email que receberá o nome e o nível.
                                  # O comando tupla[chave[1]] o número 1 representa que o que se quer é a informação que esta posição 1 da tupla_
                                  # ou seja, a tupla é enumerate(posição zer0) mais emails, no caso queremos o email.
    usuario[tupla[chave]]=[input("Digite o nome: "),
                           input("Digite o nível: ")]

for chave,dado in usuario.items():
    print("Usuário.:", chave[0])
    print("Email...:", chave[1])
    print("Nome....:", dado[0])
    print("Nível...:", dado[1])