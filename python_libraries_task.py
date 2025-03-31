import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Task 1: NumPy Array and Mean Calculation
numbers = np.arange(1, 11)  # Array from 1 to 10
mean_value = np.mean(numbers)
print(f"Mean of numbers from 1 to 10: {mean_value}")

# Task 2: Pandas DataFrame Summary Statistics
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Score": [85, 90, 95]
}
df = pd.DataFrame(data)
print("\nPandas DataFrame Summary:")
print(df.describe())

# Task 3: Fetch Data from Public API
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
if response.status_code == 200:
    api_data = response.json()
    print(f"\nFetched Data from API: {api_data['title']}")
else:
    print("\nFailed to fetch data from API")

# Task 4: Matplotlib Line Graph
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Graph")
plt.show()
