import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("test.csv",sep = ",")
missing_data = data.isnull().sum()


plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(data['Square'], bins=30, color='blue')
plt.title('Гистограмма Square')

plt.subplot(1, 2, 2)
plt.boxplot(data['Square'], vert=False)
plt.title('Ящик с усами Square (логарифмическая шкала)')

data['Square'].fillna(data['Square'].mean(), inplace=True)
room_counts = data['Rooms'].value_counts()
pivot_table = pd.pivot_table(data, values='Id', index='DistrictId', columns='Rooms', aggfunc='count', fill_value=0)
data.to_csv('surname.csv', index=False)
plt.figure(figsize=(12, 6))
plt.imshow(pivot_table, cmap='coolwarm')
plt.colorbar()
plt.title('Количество квартир в районах по числу комнат')
plt.xlabel('Комнаты')
plt.ylabel('Районы')

plt.show()