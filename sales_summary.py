product_name = input("Enter the product name: ")
sales_january = float(input("Enter January sales: "))
sales_february = float(input("Enter February sales: "))
sales_march = float(input("Enter March sales: "))

total_sales = sales_january + sales_february + sales_march
average_sales = total_sales / 3

print("\nSales Summary")
print("-------------")
print(f"Product: {product_name}")
print(f"Total sales: {total_sales}")
print(f"Average monthly sales: {average_sales}")