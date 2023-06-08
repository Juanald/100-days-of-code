import sys
from art import logo
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2
    
def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

ops = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}

def printOps(ops):
    for op in ops:
        print(op)

def calc():
    num1 = float(input("What is your first number?: "))
    endOfCalc = False
    while not endOfCalc:
        printOps(ops)
        op = input("Choose an operation: ")
        num2 = float(input("What is your second number?: "))
        answer = ops[op](num1, num2)
        print(f"{num1} {op} {num2} = {answer}")
        again = input(f"Type 'y' to use {answer} in calculation, 'n' to start a new calculation, or 'q' to quit the program.").lower()
        if again == 'y':
            num1 = answer
        elif again == 'n':
            calc()
        else:
            endOfCalc = True
            print("Thanks for using the calculator!")
            sys.exit(0)

if __name__ == "__main__":
    print(logo)
    calc()