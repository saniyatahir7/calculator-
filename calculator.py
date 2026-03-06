print ("Hello World")
print("Simple Calculator")
print("------------------")
num1 = float(input("Enter first number:"))
operator = input("Enter operator(+,-,*,/): ")
num2 = float(input("Enter second number:"))
if operator == "+":
    print("Result:",num1 + num2)
elif operator == "-":    
    print("Result:,num1-num2")
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:",num1/num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")  
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

while True:
    print("\n--- SIMPLE CALCULATOR ---")
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")
    print("5) Exit")
    choice = input("choose an option(1-5):")
    if choice == "5":
       print("Calculator closed.")
       break
    if choice not in ["1","2","3","4"]:
        print("Invalid choice.Please choose 1-5.")  
        continue
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
    if choice == "1":
        print("Result:", add(num1, num2))   
        continue
    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:" ,subtract(num1, num2))
    elif choice == "4":
        print("Result:", divide(num1, num2)) 
import random
number = random.randint(1, 10)
attempts = 0
while True:
    guess = int(input("Guess the number(1-10): "))
    attempts += 1
    if guess == number:
        print("Correct! You guessed it in", attempts,"tries.")
        break
    elif guess > number:
        print("Too high.")
    else:
        print("Too low.")                    