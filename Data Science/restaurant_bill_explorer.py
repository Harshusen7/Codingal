import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
df = df.dropna()
print(df.head())
print(df.info())

sns.barplot(x='day' , y='total_bill' , hue='sex', data=df)
plt.title('Average Total Bill per Day by Gender')
plt.xlabel('Day')
plt.ylabel('Average Bill ($)')
plt.show()

sns.countplot(x='day' , hue='sex' , data= df)
plt.title('Number of diners per day by gender')
plt.xlabel('Day')
plt.ylabel('Count')
plt.show()

sns.boxplot(x='day' , y='total_bill' , data=df)
plt.title('Spread of total bill per day')
plt.xlabel('Day')
plt.ylabel('total Bill ($)')
plt.show()

sns.stripplot(x='day' , y='total_bill' , data=df , jitter=True)
plt.title('every bill amount per day (Strip plot)')
plt.xlabel('Day')
plt.ylabel('total Bill ($)')
plt.show()

sns.swarmplot(x='day' , y='total_bill' , data=df)
plt.title('every bill amount per day (Swarm plot)')
plt.xlabel('Day')
plt.ylabel('total Bill ($)')
plt.show()

sns.jointplot(x='total_bill', y='tip', data=df, kind='kde')
plt.suptitle('Total_bill vs Tip', y=1.02)
plt.show()

sns.pairplot(df[['total_bill', 'tip', 'size']])
plt.suptitle('Pair plot - bill, Tip and Party size', y=1.02)
plt.show()