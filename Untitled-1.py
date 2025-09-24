import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
PATH_TO_FILE: str = '/content/Coffe_sales.csv'
df = pd.read_csv(PATH_TO_FILE)
df
df.head()
df.info()
df.describe()
print(df.dtypes)
for column in df.columns:
    print(f'{column}: {df[column].nunique()} уникальных значений')
sns.histplot(df['alcohol'], kde=True)
plt.title('Распределение Alcohol')
plt.xlabel('Alcohol')
plt.ylabel('Частота')
plt.show()
sns.countplot(x='quality', data=df)
plt.title('Распределение quality')
plt.xlabel('quality')
plt.ylabel('Количество')
plt.show()
sns.boxplot(x=df['chlorides'])
plt.title('Boxplot chlorides')
plt.xlabel('chlorides')
plt.show()
# Корреляционная матрица
correlation_matrix = df.corr()

# Визуализация тепловой карты
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Корреляционная матрица')
plt.show()
# test

#Falsee