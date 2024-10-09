with open('arquivos/arquivo3.txt', 'w') as arquivo:
    arquivo.write('Realizando um teste.\n')
    arquivo.writelines(['Linha 1\n', 'Linha 2\n'])