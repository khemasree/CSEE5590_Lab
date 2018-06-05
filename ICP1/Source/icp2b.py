n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
if n1%n2==0 :
    quotient= str(n1//n2)
    print("Quotient is" + quotient +" and remainder is 0")
else:
    remainder= str(n1% n2)
    quotient=str(n1//n2)
    print("Quotient is" + quotient + " and remainder is"+ remainder)


