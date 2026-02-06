num1= float(input("Enter the first number: "))
num2= float(input("Enter the second number: "))

print("Its Shruu..!")
print("\nChoose an operation: ")
print("+  for addition")
print("-  for subtraction")
print("*  for multiplication")
print("/  for division  ")

op=input("Enter your choice: ")

if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    if num2 !=0:
        result = num1 /num2
    else:
        result = "Error: Division by Zero!"
else:
    result = "Invalid choice entered! "

print(f"\nResult: {result}")
