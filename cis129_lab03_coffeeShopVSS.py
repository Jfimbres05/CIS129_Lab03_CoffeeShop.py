# Text-based Coffee Shop sim that allows a user to input two values to output an order summary in receipt form.

# Prices of items + croissant and breakfast sandwich.
coffee_price = 5.00
muffin_price = 4.00
croissant_price = 3.50
breakfastsandwichpr_price = 7.00
tax_rate = 0.06 # Taxed 6%

# Greet and ask for input + croissant and breakfast sandwich.
print("Hello! What will you be ordering today?")
num_coffees = int(input("Coffee amount: "))
num_muffins = int(input("Muffin amount: "))
num_croissant = int(input("Croissant amount: "))
num_breakfastsandwichpr = int(input("Premium Breakfast Sandwich amount: "))

# Calculating costs + croissant and breakfast sandwich.
coffee_total = num_coffees * coffee_price
muffin_total = num_muffins * muffin_price
croissant_total = num_croissant * croissant_price
breakfastsandwichpr_total = num_breakfastsandwichpr * breakfastsandwichpr_price

total = coffee_total + muffin_total + croissant_total + breakfastsandwichpr_price

# Calculate tax.
sales_tax = total * tax_rate

# Calculate the final price.
total_final = total + sales_tax

# Receipt print + croissant and breakfast sandwich + end thank you message.
print("***************************************")
      
print("My Coffee, Muffins, and More! Shop")

print("Number of coffees bought?")

print(f"{num_coffees}")

print("Number of muffins bought?")
      
print(f"{num_muffins}")

print("Number of croissants bought?")

print(f"{num_croissant}")

print("Number of Premium Breakfast Sandwiches bought?")

print(f"{num_breakfastsandwichpr}")

print("***************************************")

print("\n***************************************")

print("My Coffee, Muffins, and More! Shop")

print(f"{num_coffees} Coffee at ${coffee_price:.2f} each: $ {coffee_total:.2f}")

print(f"{num_muffins} Muffins at ${muffin_price:.2f} each: $ {muffin_total:.2f}")

print(f"{num_croissant} Croissants at ${croissant_price:.2f} each: $ {croissant_total:.2f}")

print(f"{num_breakfastsandwichpr} Premium Breakfast Sandwich at ${breakfastsandwichpr_price:.2f} each: $ {breakfastsandwichpr_total:.2f}")

# Display tax rate as integer + format tax without zero in front.
tax_percentage = int(tax_rate * 100)  # Convert tax rate to an integer.

# Conditional formatting for tax.
formatted_tax = f"{sales_tax:.2f}"  # Format the tax to 2 decimal places.
if sales_tax < 1:
    # Remove the 0 if tax is less than 1.
    formatted_tax = formatted_tax[1:]

print(f"{tax_percentage}% tax: $ {formatted_tax}")

print("---------")

print(f"Total: $ {total_final:.2f}")

print("\nThank you for shopping with us. Have a great day!")

print("***************************************")
