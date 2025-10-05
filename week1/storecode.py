#This is a simple store program that allows users to buy fruits and get a discount if they are CIF students
# List of items and their prices
items = ["1. apple ($1)", "2. banana ($0.5)", "3. orange ($0.75)", "4. grape ($2)", "5. mango ($1.5)"]
price = [1.00, 0.50, 0.75, 2.00, 1.50]
# Initialize variables
again = "yes"
total = 0
# Welcome message and display items for the customer
print("Welcome to the fruit store!")
print("Available fruits:")
for items in items:
    print(items)
# Loop to allow multiple purchases
while again == "yes":
    choice = int(input("Enter the number of the item you want to buy: "))
    amount = int(input("How many do you want to buy? "))
    total += price[choice - 1] * amount
    again = input("Do you want to buy another item? (yes/no) ")
# Apply discount for CIF students
discount = input("Are you a CIF Student? (yes/no) ")
if discount == "yes":
    total *= 0.9
# Display the total
print("Your total is: $", total)
