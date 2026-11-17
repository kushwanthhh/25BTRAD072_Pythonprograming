products = {} while True:
print("\n1. Add Product") print("2. Update Sales") print("3. Display Sales") print("4. Total Revenue")
print("5. Highest Selling Product") print("6. Exit")

choice = input("Enter choice: ")


if choice == "1":
name = input("Enter product name: ") quantity = int(input("Enter quantity sold: ")) price = float(input("Enter price per item: "))

products[name] = { "quantity": quantity, "price": price
}


print("Product added!")


elif choice == "2":
name = input("Enter product name: ")


if name in products:
 
quantity = int(input("Enter new quantity sold: ")) products[name]["quantity"] = quantity print("Sales updated!")
else:
print("Product not found")


elif choice == "3": print("\nProduct\tQuantity\tRevenue")

for name, details in products.items():
revenue = details["quantity"] * details["price"] print(name, "\t", details["quantity"], "\t\t", revenue)

elif choice == "4":
total = 0


for details in products.values():
total += details["quantity"] * details["price"]


print("Total Revenue:", total)


elif choice == "5":
if products:
highest = max( products,
key=lambda name: products[name]["quantity"]
)
print("Highest Selling Product:", highest)
 
print("Quantity Sold:", products[highest]["quantity"]) else:
print("No products available")


elif choice == "6": break

else:
print("Invalid choice")
