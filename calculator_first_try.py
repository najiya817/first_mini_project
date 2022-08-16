num1=int(input("enter the first number:"))
print(num1)
num2=int(input("enter the second number:"))
print(num2)
print("enter the choice:")
print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")
print("5.exit")
choice=input("select option 1,2,3,4,5:")
if choice == '1':
    print("this is an addition operation")
    print("the answer is:",num1+num2)
if choice== '2':
    print("this is a substraction operator")
    print("the answer is:",num1-num2)
if choice == '3':
    print("this is multiplication operation")
    print("the answer is:",num1*num2)
if choice == '4':
    print("this is division operation")
    print("the answer is:",num1/num2)
if choice == '5':
    print("this is a modulus operation")
    print("the answer is:",num1%num2)

