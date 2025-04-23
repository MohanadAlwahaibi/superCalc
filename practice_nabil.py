num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a secound number: "))
operation = input("SELECT + OR - OR % OR * OR / : ")
result = 0

if operation == "+":
    result = num_1 + num_2
    print(result)
elif operation == "-":
    result = num_1 - num_2
    print(result)
elif operation == "*":
    result = num_1 * num_2
    print(result)
elif operation == "%":
    result = num_1 % num_2
    print(result)
elif operation == "/":
    result = num_1 // num_2
    print(result)   
