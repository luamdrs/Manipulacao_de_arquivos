# Contando o número de colunas em um arquivo
f = open('arquivos/salarios_eua.csv', 'r')
data = f.read()
rows = data.split(',')
full_data = []

for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)
    first_row = full_data[0]
count = 0

for column in first_row:
    count += 1
print(count)