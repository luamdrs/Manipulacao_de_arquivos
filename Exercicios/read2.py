with open('arquivos/salarios_eua.csv', 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linha.strip())
