def add(num1, num2):
    return (num1 + num2)

def subtract(num1, num2):
    return (num1 - num2)

def multiply(num1, num2):
    return (num1 * num2)


def divide(num1, num2):
    return (num1 / num2)

def power(num1, num2):
    return(num1 ** num2)

print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n" \
        "5. Power")


# Take input from the user
user_input = int(input("Select operations form 1, 2, 3, 4 :"))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if user_input == 1:
    print(num1, "+", num2, "=",
                    add(num1, num2))

elif user_input == 2:
    print(num1, "-", num2, "=",
                    subtract(num1, num2))

elif user_input == 3:
    print(num1, "*", num2, "=",
                    multiply(num1, num2))

elif user_input == 4:
    if num2 != 0:
        print(num1, "/", num2, "=",
                    divide(num1, num2))
    else:
        print("Error: cannot divide by zero")
elif user_input == 5:
    print(num1, "**", num2, "=",
                    power(num1, num2))
else:
    print("Invalid input")