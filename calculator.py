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

def main():
    print("Simple Command Line Calculator - calculator.py:16")
    print("Select operation: - calculator.py:17")
    print("1. Add - calculator.py:18")
    print("2. Subtract - calculator.py:19")
    print("3. Multiply - calculator.py:20")
    print("4. Divide - calculator.py:21")

    while True:
        choice = input("Enter choice (1/2/3/4): ")
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers. - calculator.py:30")
                continue

            if choice == '1':
                print(f"Result: {add(num1, num2)} - calculator.py:34")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)} - calculator.py:36")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)} - calculator.py:38")
            elif choice == '4':
                print(f"Result: {divide(num1, num2)} - calculator.py:40")
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4. - calculator.py:42")
            continue

        next_calc = input("Do you want to perform another calculation? (yes/no): ")
        if next_calc.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
