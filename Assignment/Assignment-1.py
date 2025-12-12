print("Enter Product Details for MagicPin Listing\n")

product_id = int(input("Enter Product ID: "))
product_name = input("Enter Product Name: ")
price = float(input("Enter Price (₹): "))

categories_input = input("Enter Categories (comma-separated): ")
categories = []
for c in categories_input.split(","):
    categories.append(c.strip())

available_stock = int(input("Enter Available Stock: "))
sold_stock = int(input("Enter Sold Stock: "))
stock_details = (available_stock, sold_stock)

discount_percentage = float(input("Enter Discount Percentage (%): "))

features_input = input("Enter Product Features (comma-separated): ")
product_features = []
for f in features_input.split(","):
    product_features.append(f.strip())

supplier_name = input("Enter Supplier Name: ")
supplier_contact = input("Enter Supplier Contact Number: ")
supplier_location = input("Enter Supplier Location: ")
supplier_details = {
    "name": supplier_name,
    "contact": supplier_contact,
    "location": supplier_location
}

print("\n----- MagicPin Product Details -----\n")

print("Product ID, Name, Price:", product_id, product_name, price, sep=",")

print("Discount Offered: %.2f%%" % discount_percentage)

final_price = price - (price * discount_percentage / 100)
print(f"Product: {product_name}")
print(f"Original Price: ₹{price:.2f}")
print(f"Discount: {discount_percentage}%")
print(f"Price After Discount: ₹{final_price:.2f}")
print(f"Categories: {', '.join(categories)}")
print(f"Available Stock: {stock_details[0]} | Sold: {stock_details[1]}")
print(f"Features: {', '.join(product_features)}")

print("\nSupplier Details: Name - {name}, Contact - {contact}, Location - {location}".format(
    name=supplier_details["name"],
    contact=supplier_details["contact"],
    location=supplier_details["location"]
))

print("Data successfully captured using all data types and formatting methods!")

