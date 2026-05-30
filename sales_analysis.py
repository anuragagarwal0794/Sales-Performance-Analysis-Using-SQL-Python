import pandas as pd
from sqlalchemy import create_engine

password = "0794"

engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost/sales_analysis"
)

df = pd.read_sql("SELECT * FROM sales", engine)

print("Total Revenue:", df['total_amount'].sum())
print("Total Quantity Sold:", df['quantity'].sum())

print("\nTop 5 Products by Revenue:")
print(
    df.groupby('product')['total_amount']
      .sum()
      .sort_values(ascending=False)
      .head(5)
)
import matplotlib.pyplot as plt

top_products = (
    df.groupby('product')['total_amount']
      .sum()
      .sort_values(ascending=False)
      .head(5)
)

top_products.plot(kind='bar')

plt.title("Top 5 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()

plt.show()
city_sales = (
    df.groupby('city')['total_amount']
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
city_sales.plot(kind='bar')

plt.title("City-wise Revenue")
plt.xlabel("City")
plt.ylabel("Revenue")
plt.tight_layout()

plt.show()
category_sales = (
    df.groupby('category')['total_amount']
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
category_sales.plot(kind='bar')

plt.title("Category-wise Revenue")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.tight_layout()

plt.show()
plt.savefig("top_products.png")
print(
    df.groupby('city')['total_amount']
      .sum()
      .sort_values(ascending=False)
      .head(5)
)
print(
    df.groupby('category')['total_amount']
      .sum()
      .sort_values(ascending=False)
)
avg_order = df['total_amount'].mean()
print("Average Order Value:", round(avg_order, 2))
highest_product = (
    df.groupby('product')['total_amount']
      .sum()
      .idxmax()
)

print("Highest Revenue Product:", highest_product)