resposta="S"

while resposta=="S":
    nome=input("Digite o nome: ")
    idade=int(input("Digite a idade: "))
    doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa? S ou N ").upper()

    # PRIMEIRO PROBLEMA A SER RESOLVIDO
    while doenca_infectocontagiosa!="S" and doenca_infectocontagiosa!="N":
        print("Responda com S ou N")
        doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa? S ou N ").upper()
    if doenca_infectocontagiosa=="S":
        print("Encaminhe o paciente para sala AMARELA")
    else:
        print("Encaminhe o paciente para sala BRANCA")

    # SEGUNDO PROBLEMA A SER RESOLVIDO
    if idade >= 65:
        print("Paciente COM prioridade")
    else:
        genero=input("Digite o gênero do paciente F ou M: ").upper()
        while genero!="F" and genero!="M":
            print("Responda com F ou M")
            genero=input("Digite o gênero do paciente: ").upper()
        if genero=="F" and idade>10:
            gravidez=input("A paciente está grávida? S ou N ").upper()
            while gravidez!="S" and gravidez!="N":
                print("Responda com S ou N")
                gravidez=input("A paciente está grávida? S ou N ").upper()
            if gravidez=="S":
                print("Paciente COM prioridade")
            else:
                print("Paciente SEM prioridade")
        else:
            print("Paciente SEM prioridade")
    resposta=input("Se deseja cadastrar outro paciente digite S ").upper()
print("Concluído")