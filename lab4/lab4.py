csv_data = pd.read_csv('wine-quality-white-and-red.csv')
csv_data.info()

# Show quality
csv_data.corr()['quality']

# Deleting the index
csv_data = csv_data.iloc[:,1:]
print(csv_data.head())

# Show values equal to null
csv_data.isna().sum()

# Show the unique values of the "quality" column
csv_data['quality'].unique()

csv_data.hist(bins = 25,figsize = (10, 10))
plt.show()

# Check the value of alcohol can change the quality.
plt.figure(figsize = [10,6])
plt.bar(csv_data['quality'], csv_data['alcohol'], color = 'red')
plt.xlabel('quality')
plt.ylabel('alcohol')

# Assign unique values to the alcohol parameter.
alcohol = csv_data['alcohol'].value_counts()
alcohol.plot(kind = 'bar')

# Assign unique values to the acid parameter.
acidity = csv_data['fixed acidity'].value_counts()
acidity.plot(kind = 'bar')

# Assign unique values to the volacidity parameter.
volacidity = csv_data['volatile acidity'].value_counts()
volacidity.plot(kind = 'bar')
csv_data.describe()
csv_wine = pd.read_csv('wine-quality-white-and-red.csv')
csv_wine

# Analyze the types of wine
wine_types_count = csv_wine['type'].value_counts()
wine_types_count
plt.hist(csv_wine['fixed acidity'])

# pH
csv_wine['pH'].plot(kind = 'hist');

# Show alcohol properties
csv_wine['alcohol'].plot(kind = 'hist');
