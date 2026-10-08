cart = ["apple", "milk", "bread", "apple", "eggs", "milk"]

# Remove duplicate items
cart = list(set(cart))

# Add "cheese"
cart.append("cheese")

# Remove "bread"
cart.remove("bread")

# Sort alphabetically
cart.sort()

print("Final cart:", cart)
print("Number of different items:", len(cart))