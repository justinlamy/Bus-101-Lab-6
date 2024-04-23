# sales for 2023, by quarter Q1-Q4
sales_2023 = [50582, 55912, 52736, 67890]
# growth rates for 2024, by quarter Q1-Q4
growth_rates_2024 = [0.052, 0.04, 0.03, 0.02]

def predict_sales(sales_2023, growth_rates_2024):
    projected_sales_2024 = []
    for i in range(len(sales_2023)):
        projected_sale = sales_2023[i] * (1 + growth_rates_2024[i])
        projected_sales_2024.append(projected_sale)
    return projected_sales_2024

def highest_sales(sales_2023):
    highest_quarter = sales_2023.index(max(sales_2023)) + 1
    return highest_quarter

# Call the functions and pass in the appropriate values
projected_sales = predict_sales(sales_2023, growth_rates_2024)
highest_quarter = highest_sales(sales_2023)

# Display the projected sales for 2024
print("Projected Sales for 2024:")
for i in range(len(projected_sales)):
    print(f"Quarter {i+1}: {projected_sales[i]}")

# Display the quarter with the highest sales in 2023
print(f"\nThe quarter with the highest sales in 2023 is Quarter {highest_quarter}.")

