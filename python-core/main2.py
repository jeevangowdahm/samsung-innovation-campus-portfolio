
import arithmetic

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\n1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Choose operation (1-4): ")

if choice == "1":
    print("Result:", arithmetic.add(a, b))
elif choice == "2":
    print("Result:", arithmetic.subtract(a, b))
elif choice == "3":
    print("Result:", arithmetic.multiply(a, b))
elif choice == "4":
    print("Result:", arithmetic.divide(a, b))
else:
    print("Invalid choice")
    
    
import random
print(random.random())
print(random.uniform(1.5, 10))
print(random.uniform(10, 1.5))