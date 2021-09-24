with open("teste.txt","w") as arquivo:
    #conteudo = arquivo.read() # Para abrir o arquivo
    arquivo.write("Nunca foi tão fácil criar um arquivo.")

with open("teste.txt","a") as arquivo:
    arquivo.write("\nContinuação do texto.")