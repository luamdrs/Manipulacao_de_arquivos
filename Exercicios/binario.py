# Manipulação de arquivos binários
with open('arquivos/imagem.png', 'rb') as arquivo_bin:
    dados = arquivo_bin.read()

# Faz uma copia do arquivo/img
with open ('arquivos/copiaimg.png', 'wb') as arquivo_bin:
    arquivo_bin.write(dados)