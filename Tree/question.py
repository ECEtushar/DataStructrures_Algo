"""
You are making a ticketing system.
The price of a single ticket is $100.
For children under 3 years of age, the ticket is free.
Your program needs to take the ages of 5 passengers as input and output the total price for their tickets.
"""
total_price = 0
for i in range(1,6):
    age = int(input(f"Enter the age of passenger {i}: "))
    if age>3:
        total_price = total_price + 100

print(f"Your total price is {total_price}")