# Abrindo o arquivo para leitura
arq1 = open('arquivos/arquivo1.txt', 'r') # -> read

# Lendo o arquivo
print(arq1.read())

# Contar o numero de caracteres
print(arq1.tell())

# Retornar para o inicio do arquivo
print(arq1.seek(0, 0))

# Lendo os primeiros 6 caracteres
print(arq1.read(6))