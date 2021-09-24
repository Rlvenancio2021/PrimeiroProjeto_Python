## Parte inicial ##
# Declaração de Variável

nome=input("Digite um funcinário: ")
empresa=input("Digite a instituição: ")
qtde_funcionarios=int(input("Digite a qtde de funcionários: "))
mediaMensalidade=float(input("Digite a média da mensalidade: "))
# A função "input" é utilizada para solicitar ao usuário que digite a informação desejada, esta função retorna um dado no
#formato TEXTO, caso seja necessário que o dado esteja em outro formato é necessário realizar a converção
#ex valor=int(input(...)) - int é referente a números inteiros.


## Parte Final ##
responsavel=input("Digite o nome do responsável: ")
# Criar a variável -> funcionario=input("Digite o nome do funcionário: ") ou usar a variável "nome" já existente
evento=input("Digite o nome do evento: ")
valor=float(input("Digite o valor que será ressarcido: "))
## Comando para demonstrar na tela ##
print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionarios.")
print("A média da mensalidade é de: " + str(mediaMensalidade))
# função "str" é para converter o conteúdo da variável "float" para uma string
print("=====Declaração para o responsável=====")
print("Declaro para o senhor " + responsavel + ", que o senhor " + nome + " esteve presente no evento " + evento +
      " e gastou o valor de R$ " + str(valor) + " com a entrada.")
print("===============Verifique os tipos de dados abaixo:===================")
print("O tipo de dado da variavel [nome] é: ",type(nome))
print("O tipo de dado da variavel [empresa] é: ",type(empresa))
print("O tipo de dado da variavel [qtde_funcionarios] é: ",type(qtde_funcionarios))
print("O tipo de dado da variavel [mediaMensalidade] é: ",type(mediaMensalidade))
print("O tipo de dado da variavel [responsavel] é: ",type(responsavel))
print("O tipo de dado da variavel [evento] é: ",type(evento))
print("O tipo de dado da variavel [valor] é: ",type(valor))