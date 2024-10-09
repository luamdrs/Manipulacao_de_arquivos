# Gerenciando Exceções
try:
    with open('arquivos/arquivo4.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print('Arquivo encontrado.')
except FileNotFoundError:
    print('Arquivo não encontrado.')