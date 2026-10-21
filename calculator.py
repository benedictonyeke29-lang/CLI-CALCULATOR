print("Welcome to my CLI Calculator!")
print("I can help you do calculations.")


while True:
   try:
       number1 = float(input("Enter your first number: "))
       operator = input("Enter an operator (+, -, *, /): ").strip()
       number2 = float(input("Enter your second number: "))


       if operator == "+":
           result = number1 + number2
       elif operator == "-":
           result = number1 - number2
       elif operator == "*":
           result = number1 * number2
       elif operator == "/":
           if number2 == 0:
               print("Error: Cannot divide by zero.")
               continue
           result = number1 / number2
       else:
           print("Error: Invalid operator. Select either +, -, *, /")
           continue


       print(f"Result: {result:g}")


   except ValueError:
       print("Error: Please enter valid numbers.")


   again = input(
       "Do you want to calculate again? (yes/no): "
   ).strip().lower()


   if again != "yes":
       print("Thank you for using my CLI Calculator!")
       break