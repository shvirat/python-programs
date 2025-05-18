# This program prints the Fibonacci series up to n terms using a while loop
num = int(input("Enter the number of terms in the Fibonacci series: "))
a = 0
b = 1
print("Fibonacci series: ",a,b,end=" ")
i = 2
while i < num:
    c = a + b
    print(c, end=" ")
    a = b
    b = c
    i += 1
print("\nDone!")