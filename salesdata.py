#Data Analysis on CSV Files
#Import libraries
import pandas as pd
import matplotlib.pyplot as plt
#read or open csv file
data = pd.read_csv('sales.csv')
#Show the data
print("First 5 rows of the dataset:")
print(data.head())
#calculate 
sales_by_product = data.groupby('Product')['Sales'].sum()
#for bar graph
plt.figure(figsize=(8,5))
sales_by_product.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
sales_by_region = data.groupby('Region')['Sales'].sum()
print("\nTotal Sales by Region:")
print(sales_by_region)
