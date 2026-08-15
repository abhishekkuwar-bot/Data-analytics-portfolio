import pandas as pd

# Sample sales data
data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile"],
    "Region": ["East", "West", "North", "South", "East"],
    "Sales": [75000, 45000, 30000, 82000, 52000],
    "Quantity": [2, 5, 3, 2, 4]
}

df = pd.DataFrame(data)

print("=== SALES DATA ===")
print(df)

print("\n=== TOTAL SALES ===")
print(df["Sales"].sum())

print("\n=== TOTAL QUANTITY ===")
print(df["Quantity"].sum())

print("\n=== SALES BY PRODUCT ===")
print(df.groupby("Product")["Sales"].sum())

print("\n=== SALES BY REGION ===")
print(df.groupby("Region")["Sales"].sum())
print("\n=== KEY PERFORMANCE INDICATORS ===")

total_sales = df["Sales"].sum()
total_quantity = df["Quantity"].sum()
average_sales = pd.to_numeric(df["Sales"], errors="coerce").mean()
highest_sale = df["Sales"].max()

print("Total Sales:", total_sales)
print("Total Quantity:", total_quantity)
print("Average Sale:", average_sales)
print("Highest Single Sale:", highest_sale)
print("\n=== SALES DATA TYPE ===")
print(df["Sales"].dtype)
print(df["Sales"].head())
print("\n=== PRODUCT-WISE SALES ANALYSIS ===")

product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)

print(product_sales)
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()

plt.show()
print("\n=== REGION-WISE SALES ANALYSIS ===")

region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

print(region_sales)

plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()

plt.show()
# Add Order Date for monthly analysis
df["Order_Date"] = pd.date_range(
    start="2025-01-01",
    periods=len(df),
    freq="D"
)

print("\n=== ORDER DATES ADDED ===")
print(df[["Order_Date", "Product", "Sales"]].head())
print("\n=== MONTHLY SALES ANALYSIS ===")

monthly_sales = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"]
    .sum()
)

print(monthly_sales)

plt.figure(figsize=(10, 5))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
print("\n=== REGION SALES CONTRIBUTION ===")

region_sales = df.groupby("Region")["Sales"].sum()

region_percentage = (region_sales / region_sales.sum()) * 100

print(region_percentage.round(2))