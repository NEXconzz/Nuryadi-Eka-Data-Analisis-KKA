import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# FIX: tambahkan delimiter pemisah
data = pd.read_csv('nilai_siswa.csv', sep=';')

print(data.head())
print(data.info())
print(data.describe())

print("Rata-rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])

matematika = data[data['Mapel'] == "Matematika"]
print(matematika)

data.groupby('Mapel')['Nilai'].agg(["max", 'min'])

rata = data.groupby('Mapel')['Nilai'].mean()
rata.plot(kind='bar')
plt.title('Rata-Rata Nilai per Mapel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.show()

sns.boxplot(x='Mapel', y='Nilai', data=data)
plt.title('Distribusi Nilai per Mapel')
plt.show()
