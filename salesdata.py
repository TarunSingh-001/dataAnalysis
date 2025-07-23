# Task 5: Data Analysis on CSV Files
# I have written this code to analyze a sales CSV file using pandas and matplotlib.

# Step 1: Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Load the CSV file
# Make sure your sales.csv is in the same folder or upload it in Colab
data = pd.read_csv('sales.csv')

# Step 3: Show the first few rows to understand the data
print("First 5 rows of the dataset:")
print(data.head())

# Step 4: Group the data by Product and calculate total sales
sales_by_product = data.groupby('Product')['Sales'].sum()

# Step 5: Plot the sales using a bar chart
plt.figure(figsize=(8,5))
sales_by_product.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 6: You can also do group by Region or Date for more insights
# Here's another example: sales by Region
sales_by_region = data.groupby('Region')['Sales'].sum()
print("\nTotal Sales by Region:")
print(sales_by_region)
