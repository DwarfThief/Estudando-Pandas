import pandas as pd

# df significa DataFrame
df = pd.read_csv('./Sample-Data/intel.csv')

# Imprimindo df para ter certeza que o Pandas abriu o intel.csv
# print(df)

# Imprime o nome das colunas
# print(df.columns)

# Imprime das linhas 0 às i, nesse caso, 10
# print(df.head(10))

# Imprime das linhas finais para cima
# print(df.tail(10))

# Imprime as informações do documento, como os valores das colunas, etc
# print(df.info())

# Selecionar toda a coluna chamada X
# X = df['X']
# open = df['Open']
# print(open)

# Imprime as duas colunas com o nome passado no param
# print(df[['Open', 'Close']])

# Imprime a descricao do arquivo, com valor max, min e as medias de valores. Tudo por coluna
# print(df.describe())

# Checando quais valores da coluna são > 40
# print(df['Open'] > 40)

# Retorna apenas aqueles que cumprem a condição
# print(df[df['Open']>40])

