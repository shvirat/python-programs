# This program converts temperature between Celsius and Fahrenheit
print("Enter 1 for Celsius to Fahrenheit conversion")
print("Enter 2 for Fahrenheit to Celsius conversion")
choice = int(input("Enter your choice: "))
if choice == 1:
    c = float(input("Enter temperature in celsius: "))
    f = (c * 9/5) + 32
    print("Temperature in Fahrenheit: ", f)
elif choice == 2:
    f = float(input("Enter temperature in fahrenheit: "))
    c = (f -32) * 5/9
    print("Temperature in celsius: ", c)
else:
    print("You have entered an invalid choice")
print("Thank you for using the temperature converter!")