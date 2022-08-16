
print("**************    WElCOME TO ZODIAC CALCULATOR    ***************")

flag=False
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
replace=""
choice=input("select option 1,2,3,4,5:")
if choice == '1':
    replace1="Addition"
    result=num1+num2
if choice== '2':
    if num1<num2:
        flag=False
        print("cannot subtract ,coz first number is less than the second number")
    else:
        flag=True
        replace1="Subtraction"
        result=num1-num2
if choice == '3':
    replace1="Multiplication"
    result=num1*num2
if choice == '4':
    replace1="Division"
    result=num1//num2
if choice == '5':
    replace1="Modulus"
    result=num1%num2
if flag==True:
    print("The result of",replace1,"of",num1,"and",num2,"is",result)

