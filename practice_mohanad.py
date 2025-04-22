x =int(input("input the first value: "))
y =int(input("input the second value: "))
z =input("select * OR /: ")
result = 0

if z == "*" :
    result = x * y
    print("the result is: ", result)
elif z == "/" :
    result = x // y 
    print("the result is: " , result)
