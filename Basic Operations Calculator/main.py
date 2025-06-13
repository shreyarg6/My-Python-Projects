def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 /n2

calc = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for symbol in calc:
    print(symbol)
operation_symbol = input("Pick and operation from above: ")
calculation_function = calc[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")