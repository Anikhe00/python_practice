import calculator

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
result = 0

match operation:
  case "+":
    result = calculator.add(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")
  case "-":
    result = calculator.subtract(num1, num2)
    print(f"The difference between {num1} and {num2} is {result}")
  case "*":
    result = calculator.multiply(num1, num2)
    print(f"The product of {num1} and {num2} is {result}")
  case "/":
    if num2 != 0:
      result = round(calculator.divide(num1, num2), 2)
      print(f"The quotient of {num1} and {num2} is {result}")
    else:
      print(f"Cannot divide by zero.")
  case _:
    print("Invalid operator.")