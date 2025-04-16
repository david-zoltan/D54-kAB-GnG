import sys
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error: Cannot calculate square root of negative number"
    return math.sqrt(x)

def main():
    print("Simple CLI Calculator")
    print("Available operations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (^)")
    print("6. Square Root (√)")
    print("7. Exit")

    while True:
        try:
            choice = input("\nEnter operation number (1-7): ")
            
            if choice == '7':
                print("Goodbye!")
                sys.exit(0)
            
            if choice not in ['1', '2', '3', '4', '5', '6']:
                print("Invalid choice. Please select 1-7.")
                continue

            if choice == '6':  # Square root only needs one number
                num1 = float(input("Enter number: "))
                result = square_root(num1)
                print(f"Result: √{num1} = {result}")
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    result = add(num1, num2)
                    print(f"Result: {num1} + {num2} = {result}")
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"Result: {num1} - {num2} = {result}")
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"Result: {num1} * {num2} = {result}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"Result: {num1} / {num2} = {result}")
                elif choice == '5':
                    result = power(num1, num2)
                    print(f"Result: {num1} ^ {num2} = {result}")

        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit(0)

if __name__ == "__main__":
    main() 