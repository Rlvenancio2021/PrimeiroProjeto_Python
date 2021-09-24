from PrimeiroProjeto.Capitulo3_Funcoes.IdentificadorDeFuncoes import *

minhaLista=[]
print("Preenchendo")
preencherInventario(minhaLista)
print("Exibindo")
exibirInventario(minhaLista)

print("Pesquisando")
localizarPorNome(minhaLista)
print("Alterando")
depreciarPorNome(minhaLista, 20) #O segundo parâmetro defini o percentual da depreciação.

print("Excluindo")
print(excluirPorSerial(minhaLista)) #a função excluir serial esta dentro do print por possuir um retorno.
exibirInventario(minhaLista) #mesma função chamada duas vezes economizando linhas de código.

print("Resumindo")
resumirValores(minhaLista)