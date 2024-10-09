# Abrindo dataseat em linha unica
f = open('arquivos/salarios_eua.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows)