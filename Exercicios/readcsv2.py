# Dividindo um arquivo em colunas
f = open('arquivos/salarios_eua.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)
print(full_data)