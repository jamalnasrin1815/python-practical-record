import pandas as pd
import numpy as np

# Sales data
sales = [10000, 15000, 12000, 18000, 22000, 16000, 25000]

df = pd.DataFrame({
    "Sales": sales
})

print("===== SALES DATA =====")
print(df)

# NumPy statistical calculations
mean_sales = np.mean(sales)
median_sales = np.median(sales)
maximum_sales = np.max(sales)
minimum_sales = np.min(sales)
std_sales = np.std(sales)

print("\n--- Statistical Analysis ---")
print("Mean Sales:", mean_sales)
print("Median Sales:", median_sales)
print("Maximum Sales:", maximum_sales)
print("Minimum Sales:", minimum_sales)
print("Standard Deviation:", round(std_sales, 2))