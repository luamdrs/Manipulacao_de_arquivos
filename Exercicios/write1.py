# Abrindo arquivo para gravação
arq2 = open('arquivos/arquivo2.txt', 'w') # -> write

# Como abrimos o arquivo apenas para gravação, não podemos usar comandos de leitura.
# io.UnsupportedOperation: not readable
# print(arq2.read())

# Gravação do arquivo
arq2.write('Aprendendo a programar em Python.')
arq2.close()

# Lendo arquivo gravado
arq2 = open('arquivos/arquivo2.txt', 'r')
print(arq2.read())

# Acrescentando conteudo
arq2 = open('arquivos/arquivo2.txt', 'a') # a -> append
arq2.write('\nVenha aprender voce tambem!')
arq2.close()

arq2 = open('arquivos/arquivo2.txt', 'r')
print(arq2.read())

# Retornando ao inicio do arquivo para leitura
arq2.seek(0, 0)

print(arq2.read())