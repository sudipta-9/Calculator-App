import math

def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

def power(a, b):
  return math.pow(a, b)

def square_root(a):
  return math.sqrt(a)

def log(a, b):
  return math.log(a, b)

def main():
  print("Welcome to the professional calculator!")

  while True:
    print("What would you like to do? (1) Add (2) Subtract (3) Multiply (4) Divide (5) Power (6) Square root (7) Logarithm")

    choice = input("Enter your choice: ")

    if choice == "1":
      a = float(input("Enter the first number: "))
      b = float(input("Enter the second number: "))
      print(f"{a} + {b} = {add(a, b)}")

    elif choice == "2":
      a = float(input("Enter the first number: "))
      b = float(input("Enter the second number: "))
      print(f"{a} - {b} = {subtract(a, b)}")

    elif choice == "3":
      a = float(input("Enter the first number: "))
      b = float(input("Enter the second number: "))
      print(f"{a} * {b} = {multiply(a, b)}")

    elif choice == "4":
      a = float(input("Enter the first number: "))
      b = float(input("Enter the second number: "))
      print(f"{a} / {b} = {divide(a, b)}")

    elif choice == "5":
      a = float(input("Enter the base number: "))
      b = float(input("Enter the exponent: "))
      print(f"{a} ^ {b} = {power(a, b)}")

    elif choice == "6":
      a = float(input("Enter the number: "))
      print(f"The square root of {a} is {square_root(a)}")

    elif choice == "7":
      a = float(input("Enter the number: "))
      b = float(input("Enter the base: "))
      print(f"The logarithm of {a} to the base {b} is {log(a, b)}")

    else:
      print("Invalid choice.")

if __name__ == "__main__":
  main()
