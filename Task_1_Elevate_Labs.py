import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('netflix_titles.csv' , lineterminator = "\n")

print(df.head()) # Prints the first 5 rows of the data.

# **Identify and handle null values.**

print(df.isnull().sum()) # Prints the count of null values.

# This fills 'NA' where null values are.

df["country"] = df["country"].fillna("Unknown") 
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown") 

# **Checks if there any duplicate values.**

print(df.duplicated()) # Checks whether there are duplicate values or not.

df_duplicates_drops = df.drop_duplicates() # This removes duplicate values if there any, in this case there are not any duplicates.

df.to_csv('your_file.csv', mode='a', header=False, index=False)
# Data Visualization

sns.set_style("whitegrid")

print(df["rating"].describe())

# Creating the chart for rating count using seaborn library.
sns.catplot(y = "rating", data = df, kind = "count", order = df["rating"].value_counts().index, color = "#4287f5")

# Using matplotlib library
plt.title("Rating Column Distribution") # Gives title to the visualization
plt.show()

'''Summary or Insights from the dataset:

1. Importing python libraries like Pandas, Matplotlib, Seaborn

2. Read the csv file from pandas method read_csv()

3. Identify the null values and fills them with Unknown string.

4. Checks for duplicate values but there are no duplicate values. 

5. Lastly, make visualization of rating column distribution after cleaning the data.

'''
