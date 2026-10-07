import pandas as pd
import numpy as np

# Create sales dataset
data = {
    "Product": [
        "Laptop", "Phone", "Tablet",
        "Laptop", "Phone", "Tablet",
        "Laptop", "Phone"
    ],
    "Quantity": [2, 5, 3, 4, 6, 5, 3, 7],
    "Price": [50000, 20000, 15000,
              50000, 20000, 15000,
              50000, 20000]
}

df = pd.DataFrame(data)

# Calculate revenue
df["Revenue"] = df["Quantity"] * df["Price"]

print("========== SALES DATA ANALYSIS ==========")
print(df)

# -----------------------------
# Statistical Analysis
# -----------------------------

total_revenue = np.sum(df["Revenue"])
average_revenue = np.mean(df["Revenue"])
median_revenue = np.median(df["Revenue"])
maximum_revenue = np.max(df["Revenue"])
minimum_revenue = np.min(df["Revenue"])

print("\n========== STATISTICS ==========")
print("Total Revenue   :", total_revenue)
print("Average Revenue :", round(average_revenue, 2))
print("Median Revenue  :", median_revenue)
print("Maximum Revenue :", maximum_revenue)
print("Minimum Revenue :", minimum_revenue)

# -----------------------------
# Product Analysis
# -----------------------------

product_revenue = df.groupby("Product")["Revenue"].sum()
product_quantity = df.groupby("Product")["Quantity"].sum()

print("\n========== PRODUCT ANALYSIS ==========")
print("\nRevenue by Product:")
print(product_revenue)

print("\nQuantity Sold by Product:")
print(product_quantity)

# Best product
best_product = product_revenue.idxmax()

# Most quantity sold
most_sold_product = product_quantity.idxmax()

print("\n========== BUSINESS INSIGHTS ==========")
print("Highest Revenue Product:", best_product)
print("Most Units Sold:", most_sold_product)

# Overall standard deviation
std = np.std(df["Revenue"])

print("Revenue Standard Deviation:", round(std, 2))

if average_revenue > 100000:
    print("Insight: Sales performance is very strong.")
elif average_revenue > 50000:
    print("Insight: Sales performance is good.")
else:
    print("Insight: Sales performance needs improvement.")