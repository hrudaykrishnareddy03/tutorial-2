def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    while True:
        try:
            first_number = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ").strip()
            second_number = float(input("Enter second number: "))

            if operator == "+":
                result = add(first_number, second_number)
            elif operator == "-":
                result = subtract(first_number, second_number)
            elif operator == "*":
                result = multiply(first_number, second_number)
            elif operator == "/":
                result = divide(first_number, second_number)
            else:
                print("Invalid operator")
                continue

            print(f"Result: {result}")
        except ValueError:
            print("Please enter valid numbers.")
        except ZeroDivisionError as error:
            print(error)

        again = input("Do you want to calculate again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    calculator()
