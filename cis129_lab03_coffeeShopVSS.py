# Prices of items
coffee_price = 5.00
muffin_price = 4.00
tax_rate = 0.06 # Taxed 6%

# Greet and ask for input
print("Hello! How many coffees and how many muffins will you be ordering?")
num_coffees = int(input("Coffee amount: "))
num_muffins = int(input("Muffin amount: "))

# Calculating costs
coffee_total = num_coffees * coffee_price
muffin_total = num_muffins * muffin_price
total = coffee_total + muffin_total

# Calculate tax
sales_tax = total * tax_rate

# Calculate the final price
total_final = total + sales_tax

# Receipt print
print("***************************************")
      
print("My Coffee and Muffin Shop")

print("Number of coffees bought?")

print(f"{num_coffees}")

print("Number of muffins bought?")
      
print(f"{num_muffins}")

print("***************************************")

print("\n***************************************")

print("My Coffee and Muffin Shop Receipt")

print(f"{num_coffees} Coffee at ${coffee_price} each: $ {coffee_total:.2f}")

print(f"{num_muffins} Muffins at ${muffin_price} each: $ {muffin_total:.2f}")

# Display tax rate as integer + format tax without zero in front
tax_percentage = int(tax_rate * 100)  # Convert tax rate to an integer

# Conditional formatting for tax
formatted_tax = f"{sales_tax:.2f}"  # Format the tax to 2 decimal places
if sales_tax < 1:
    # Remove the 0 if tax is less than 1
    formatted_tax = formatted_tax[1:]

print(f"{tax_percentage}% tax: $ {formatted_tax}")

print("---------")

print(f"Total: $ {total_final:.2f}")

print("***************************************")