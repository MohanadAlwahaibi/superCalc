num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter secound number: "))
opp = input("Select + or - or * or /: ")
result = 0

if opp == "+":
    result = num_1 + num_2
elif    opp == "-":
    result = num_1 - num_2
elif    opp == "*":
    result = num_1 * num_2
elif    opp == "/":
    result = num_1 // num_2

print(num_1)
print(num_2)

print("result is: ", result)

def absolute_function():
    m = int(input("Enter a number to Check: "))
    print(abs(m))
absolute_function()

def betwise_function():
    a = (int(input("Enter first number: ")))
    b = (int(input("Enter secound number: ")))
    select_now  = input("SELECT & or | or ^")

    if select_now == "&":
        print(a & b)
    elif select_now == "|":
        print(a | b)
    elif select_now =="^":
        print(a ^ b)

betwise_function()
        