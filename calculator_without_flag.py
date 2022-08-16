
print("**************    WElCOME TO ZODIAC CALCULATOR    ***************")


num1=int(input("enter the first number:"))
print(num1)
num2=int(input("enter the second number:"))
print(num2)
print("enter the choice:")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.Modulus")
result=0
choice=input("select option 1,2,3,4,5:")
if choice == '1':
    result=num1+num2
    print("the result of addition of",num1 ,"and",num2,"is",result)
if choice== '2':
    if num1<num2:
        print("cannot subtract ,coz first number is less than the second number")
    else:
        result=num1-num2
        print("the result of subtraction of ",num1 ,"and",num2,"is",result)
if choice == '3':
    if num1==0 or num2==0:
        print("cannot multiply")
    else:
        result=num1*num2
        print("the result of ",num1 ,"and",num2,"is",result)
if choice == '4':
    if num2==0:
        print("cannot divide")
    else:
        result=num1//num2
        print("the division of ",num1,"and",num2,"is",result)
if choice == '5':
    if num2==0:
        print("cannot do modulus opeator")
    else:
        result=num1%num2
        print("The result of modulus","of",num1,"and",num2,"is",result)

