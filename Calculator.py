
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

name = input("what is your name: ")
print(f"hello dummy... i mean {name}, welcome to your calculater because you can't do simple math")

num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number now: "))

print("Choose operation: \n" \
"+,-,*,/")

choice = input("enter your choice...")

if choice == "+":
    print("the answer is", add(num1, num2),", can't even add two numbers. you might want to pay antention in school a little more.")
elif choice == "-":
    print("the answer is", subtract(num1, num2),", normal substraction, maybe someone should subtract the grade you're in so you can re-learn math.")
elif choice == "*":
    print("the answer is", multiply(num1, num2),", wow, look at you multiplying like a math genius!")
elif choice == "/":
    if num2 == 0:
        print("i have no words, stick to addition for now")
    else:
        print("the answer is", divide(num1, num2),", division? Looks like someone finally learned to share… barely.")
else:
    print("come on, i listed the options for you...")




