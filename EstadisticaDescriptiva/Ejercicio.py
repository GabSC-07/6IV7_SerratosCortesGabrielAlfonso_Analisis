import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./EstadisticaDescriptiva/housing.csv')

# MEDIA
elementos = {"longitude", "latitude", "housing_median_age", "total_rooms", "total_bedrooms", "population", "households", "median_income", "median_house_value"}

for i in elementos:
    media = df[i].mean()
    print('Media de:', media)


print(df)