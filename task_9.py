a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

print(a+b)
print(a-b)
print(a*b)

if b != 0:
    print(a/b)
    print(a//b)
    print(a%b)
else:
    print("Division by zero is not possible")

print(a**b)