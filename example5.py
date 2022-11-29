import pandas as pd

import matplotlib.pyplot as plt

titanic = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/carData/TitanicSurvival.csv')
pd.set_option('display.precision',2)

# age histogram

plt.hist(titanic.age)
plt.axvline(titanic.age.mean(),color='k', linestyle='dashed', linewidth=1)
plt.title('Ages of passengers on Titanic')
plt.ylabel('Count')
plt.xlabel('Age (in years)')
plt.show()