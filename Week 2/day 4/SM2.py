item_price = 19.99
item_count = 5
total_cost = item_price* item_count
print(f"Your total is ${total_cost:.2f} for {item_count} items.")
# Output: Your total is $99.95 for 5 items.
# You can also use the self-documenting
#expression specifier `=` for debugging
bugs = 'roaches'
count = 13
print(f"Debugging {bugs=} {count=}")
# Output: Debugging bugs='roaches' count=13
