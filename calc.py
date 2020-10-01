num1 = float(input("Enter First value : "))
op = input("Choose operator : ")
num2 = float(input("Enter Second value : "))

if op == '+':
    ans = num1 + num2
    print(f"Result is : {ans}")
elif op == '-':
    ans = num1 - num2
    print(f"Result is : {ans}")
elif op == '*':
    ans = num1 * num2
    print(f"Result is : {ans}")
elif op == '/':
    try:
        ans = num1/num2
    except ZeroDivisionError:
        print("You can't divide by 0")
    else:
        print(f"Result is : {ans}")

else:
    print("Invalid inputs!")
