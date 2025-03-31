# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets

# Step 1: Load the Dataset
# Load Iris dataset from sklearn
iris = datasets.load_iris()

# Convert to DataFrame for easier manipulation
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Step 2: Check Data Types and Missing Values
# Check for data types and missing values
print("\nDataset info:")
df.info()

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Step 3: Basic Data Analysis
# Compute basic statistics for numerical columns
print("\nBasic statistics of the dataset:")
print(df.describe())

# Group by species and calculate the average petal length
print("\nAverage petal length per species:")
print(df.groupby('species')['petal length (cm)'].mean())

# Step 4: Data Visualization

# Set the seaborn style
sns.set(style="whitegrid")

# 4.1 Line Chart: Trend of Petal Length
plt.figure(figsize=(10, 5))
plt.plot(df.index, df["petal length (cm)"], marker="o", linestyle="-", color="b")
plt.title("Trend of Petal Length")
plt.xlabel("Index")
plt.ylabel("Petal Length (cm)")
plt.show()

# 4.2 Bar Chart: Average Petal Length per Species
plt.figure(figsize=(8, 5))
sns.barplot(x="species", y="petal length (cm)", data=df, palette="pastel")
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 4.3 Histogram: Distribution of Sepal Length
plt.figure(figsize=(8, 5))
sns.histplot(df["sepal length (cm)"], bins=20, kde=True, color="green")
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4.4 Scatter Plot: Sepal Length vs. Petal Length
plt.figure(figsize=(8, 5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df, palette="coolwarm")
plt.title("Sepal Length vs. Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

# Step 5: Interpret Findings
# 1. The line chart shows trends in petal length, with distinct variations across the dataset.
# 2. The bar chart shows that Setosa species has the smallest average petal length, followed by Versicolor and Virginica.
# 3. The histogram reveals that the sepal length distribution is relatively uniform with a slight peak in the middle.
# 4. The scatter plot shows a positive relationship between sepal length and petal length, especially for Setosa.

# Step 6: Handle Errors (Optional)
# Handling errors like file not found or incorrect data types can be done as follows:

try:
    df = pd.read_csv('your_dataset.csv')
except FileNotFoundError:
    print("The dataset file was not found.")
