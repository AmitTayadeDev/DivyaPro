from Calculator import addition, subtraction, multiplication, division, modulo

def main():
    print("Calculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulo")
    
    choice = input("Enter your choice (1-5): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = addition.add(num1, num2)
        print("Result:", result)
    elif choice == '2':
        result = subtraction.subtract(num1, num2)
        print("Result:", result)
    elif choice == '3':
        result = multiplication.multiply(num1, num2)
        print("Result:", result)
    elif choice == '4':
        try:
            result = division.divide(num1, num2)
            print("Result:", result)
        except ValueError as e:
            print(e)
    elif choice == '5':
        try:
            result = modulo.modulo(num1, num2)
            print("Result:", result)
        except ValueError as e:
            print(e)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
