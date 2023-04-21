# Gold Shop Billing System with Discount

# Defining the price of gold per gram
gold_price_per_gram = 5000

# Defining the discount percentage
discount_percentage = 10

# Function to calculate the discount
def calculate_discount(price):
    discount = (price * discount_percentage) / 100
    return discount

# Function to calculate the total bill with discount
def calculate_total_bill(weight):
    total_price = weight * gold_price_per_gram
    discount = calculate_discount(total_price)
    total_bill = total_price - discount
    return total_bill

# Taking input from user
customer_name = input("Enter customer name: ")
gold_weight = float(input("Enter gold weight (in grams): "))

# Calculating the total bill with discount
total_bill = calculate_total_bill(gold_weight)

# Printing the bill
print("\n\nGold Shop Billing System\n")
print("Customer Name: ", customer_name)
print("Gold Weight (in grams): ", gold_weight)
print("Gold Price per gram: Rs.", gold_price_per_gram)
print("Discount Percentage: ", discount_percentage, "%")
print("Total Bill: Rs.", total_bill)
