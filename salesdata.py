#Data Analysis on CSV Files by using Python
#Import libraries i use
import pandas as pd
import matplotlib.pyplot as plt
#Load the CSV file
data=pd.read_csv('sales.csv')
print("rows of the dataset:")
print(data)
#give sales by product
sales_by_product=data.groupby('Product')['Sales'].sum()
print("\nSales by Product:")
print(sales_by_product)
#give sales by region
sales_by_region=data.groupby('Region')['Sales'].sum()
print("\nTotal Sales by Region:")
print(sales_by_region)
#for plotting bar graph
plt.figure(figsize=(8,5))
sales_by_product.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
