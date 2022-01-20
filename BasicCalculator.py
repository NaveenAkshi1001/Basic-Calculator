repeat='y'
print("***** BASIC CALCULATOR *****\n")
while repeat=='y':
    num1=float(input("Enter first number:"))
    operator=input("Enter your choice\n + -> addition\n - -> subtraction\n * -> multiplication\n / -> division\n")
    num2=float(input("Enter second number:"))
    if operator=='+':
       answer=num1+num2
       print(num1,'+',num2,'=',answer)
    elif operator=='-':
        answer=num1-num2
        print(num1,'-',num2,'=',answer)
    elif operator=='*':
        answer=num1*num2
        print(num1,'*',num2,'=',answer)
    elif operator=='/':
        answer=num1/num2
        print(num1,'/',num2,'=',answer)
else:
    print("Invalid,Please enter the valid operator")
    y_or_n=input("Press 'y' for another calculation")
    repeat=y_or_n.upper()
if repeat !='y':
  print("*** THANK YOU ***")
                                     
