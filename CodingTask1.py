import pandas as pd
import numpy as np
from scipy import stats as sts
import matplotlib.pyplot as plt

df = pd.read_excel("C:\\Users\\Project Codingan\\Tugas Statprob\\Dataset.xlsx")
df1 = pd.DataFrame(df, columns = ["Penjualan A (pcs)", "Penjualan B (pcs)"])
print(df.head(n = 100))
print("------Mean data------")
print(np.mean(df[["Penjualan A (pcs)"]]))
print(np.mean(df[["Penjualan B (pcs)"]]))
print("")
print("------Median data------")
print(np.median(df[["Penjualan A (pcs)"]]))
print(np.median(df[["Penjualan B (pcs)"]]))
print("")
print("------Modus data------")
print(sts.mode(df[["Penjualan A (pcs)"]]))
print(sts.mode(df[["Penjualan B (pcs)"]]))
print("")
print("------Standard Deviance------")
print(np.std(df[["Penjualan A (pcs)"]]))
print(np.std(df[["Penjualan B (pcs)"]]))
print("")
print("------Range------")
print(np.ptp(df[["Penjualan A (pcs)"]]))
print(np.ptp(df[["Penjualan B (pcs)"]]))
print("")
print("------IQR------")
print(sts.iqr(df[["Penjualan A (pcs)"]]))
print(sts.iqr(df[["Penjualan B (pcs)"]]))
print("")
print("------Variance------")
print(np.var(df[["Penjualan A (pcs)"]]))
print(np.var(df[["Penjualan B (pcs)"]]))
print("")
print("------Skewness------")
print(sts.skew(df[["Penjualan A (pcs)"]]))
print(sts.skew(df[["Penjualan B (pcs)"]]))
print("")
print("------Kurtosis------")
print(sts.kurtosis(df[["Penjualan A (pcs)"]]))
print(sts.kurtosis(df[["Penjualan B (pcs)"]]))
print("")
print("------Frequency Table------")
df1 = pd.DataFrame(df, columns = ['Penjualan A (pcs)'])
Frequency_Table = df['Penjualan A (pcs)'].value_counts().reset_index()
Frequency_Table.columns = ['Penjualan A (pcs)', 'Frequency']
Frequency_Table = Frequency_Table.sort_values('Penjualan A (pcs)')
print(Frequency_Table)
print("")
df1 = pd.DataFrame(df, columns = ['Penjualan B (pcs)'])
Frequency_Table = df['Penjualan B (pcs)'].value_counts().reset_index()
Frequency_Table.columns = ['Penjualan B (pcs)', 'Frequency']
Frequency_Table = Frequency_Table.sort_values('Penjualan B (pcs)')
print(Frequency_Table)
print("")
print("------Boxplot------")
plt.boxplot(df, vert=False)
plt.title("Boxplot")
plt.xlabel("Penjualan A (pcs)")
plt.show()
print("")