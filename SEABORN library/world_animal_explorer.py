import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('penguins')
df = df.dropna()

print("First 5 rows:")
print(df.head())
print()
print(df.info())
print()
print(df.describe())
print()
print("Species:", df['species'].unique())
print("Islands:", df['island'].unique())

sns.histplot(data=df, x='body_mass_g', bins=20, color='steelblue')
plt.title('Distribution of penguin body mass')
plt.xlabel('Body Mass (grams)')
plt.ylabel('count')
plt.show()

sns.kdeplot(data=df, x='flipper_length_mm',hue='species', fill=True)
plt.title('Flipper length Shape by species (KDE)')
plt.xlabel('Flipper Length (mm)')
plt.show()