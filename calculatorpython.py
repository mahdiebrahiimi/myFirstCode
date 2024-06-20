
print("1 add")
print("2 minus")
print("3 multiply")
print("4 devide")
print("Choose an operation:")
option = int(input("Choose an operation:"))

if(option in [1,2,3,4]):
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
   
   if(option == 1):
    print("Result:", num1 + num2)
   elif(option == 2):
    print("Result:", num1 - num2)
   elif(option == 3):
    print("Result:", num1 * num2)
   elif(option == 4):
    if(num2 != 0):

else:
    print("Invalid operation entered")

    print("The result is {}".format(result)) # type: ignore