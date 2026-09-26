import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Get seaborn datset names
print(sns.get_dataset_names())

#Load penguins dataset
df = sns.load_dataset('penguins')

# Display first 10 rows
print(df.head(10))

# Display shape
print(df.shape)

# Display last few rows
print(df.tail())

# Check for null values
print(df.isnull().sum())

# display basic statistics
print(df.describe())

# display data types
print(df.dtypes)

# display dataset info
print(df.info)

# displayall atatistics including categorial
print(df.describe(include='all'))

# Display correlation matrix
print(df.corr(numeric_only=True))

#  create heatmap of correlations
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()

# create histograms
df.select_dtypes(include=[np.number]).plot(kind='box', subplots=True, layout=(3,2), sharex=False, sharey=False, figsize=(8,12))
plt.show()

# Display value counts 
print(df.sex.value_counts())
print(df.island.value_counts())
print(df.species.value_counts())

# create count plots
sns.countplot(data=df, x='sex')
plt.show()
