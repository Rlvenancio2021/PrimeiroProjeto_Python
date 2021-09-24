#==PRIMEIRO FORMA DE CRIAR UM DICIONÁRIO==
usuarios={}
usuarios={
    "Chaves" :["Chaves Silva", "17/06/1975", "Recep_01"],
    "Quico" :["Enrico Flores", "03/06/1976", "Raiox_02"],
    "Quico" :["Enrico Flores", "03/06/1976", "Raiox_03"]
}

#==SEGUNDA FORMA DE CRIAR UM DICIONÁRIO==
#Outra forma de adicionar itens ao dicionário
#Quando queremos adicionar opjeto por objeto
usuarios["Florinda"]=["Florinda Flores", "26/11/2017", "Recep_01"]
usuarios["Florinda"]=["Florinda Flores", "26/11/2016", "Recep_01"]

#==RETORNAR OS DADOS DE UM OBJETO==
print(usuarios) #Irá exibir tudo que existe dentro do dicionário
print("##########==========##########")
print("Dados: ",usuarios.get("Chaves")) #Irá exibir somente o usuário que estiver a chave solicitada