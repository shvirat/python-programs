# This program calculates the electricity bill based on the number of units consumed.
unit = int(input("Enter the number of units consumed: "))
if unit < 0:
    print("Invalid input")
elif unit <= 150:
    bill = unit * 2.50
elif unit > 150 and unit <= 300:
    bill = (150 * 2.50) + (unit - 150) * 3.00
else:
    bill = (150 * 2.50) + (150 * 3.00) + (unit - 300) * 5.00
print("Electricity bill is: ",bill)
print("Thank you for using the electricity bill calculator!")