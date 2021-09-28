with open("economic-indicators.csv", "r") as boston:
    total=0 # variável criada para somar o total de voos.
    for linha in boston.readlines() [1:-1]: # realizar a leitura a partir da linha 1 descartando a linha do título
        total=total+float(linha.split(",")[3]) # soma todas as linhas da coluna na posição 3
    print("O total de voos é: ", total)