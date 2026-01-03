# ---Major String Manipulation Program---
# this program calculates total cost by multiplying user input price and quantity,
# then prints final results.

product_price = float(input("Enter the product price: "))
count = 7
total_cost = product_price* count
# %f manipulation
print("Your total is $%f for %d items." % (total_cost, count))

grocery_cost = float(input("Enter the grocery cost: "))
quantity = 3
total = grocery_cost* quantity
# %.2f manipulation
print("Your total cost is $%.2f for %d quantity" % (total, quantity))