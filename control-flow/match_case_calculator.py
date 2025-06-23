
def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose the operation (+, -, *, /): ")

        match operation:
            case "+":
                result = num1 + num2
                print(f"The result is {result}")
            case "-":
                result = num1 - num2
                print(f"The result is {result}")
            case "*":
                result = num1 * num2
                print(f"The result is {result}")
            case "/":
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"The result is {result}")
            case _:
                print("Invalid operation selected. Please choose one of +, -, *, /.")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")

if __name__ == "__main__":
    main()
