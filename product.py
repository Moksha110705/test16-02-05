while True:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    if num1 == -1 or num2 == -1:
        print("Exiting program...")
        break
    
    product = num1 * num2
    print(f"Product: {product}")

