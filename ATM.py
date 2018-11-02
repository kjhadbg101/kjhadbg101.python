balance=25000
print("welcome to SATHYA ATM")
pin=input("enter pin no:")
if pin=="5474":
    print("welcome")
    amt=int(input("enter amount:"))
    if (amt%100)==0:
        if amt<=10000:
            if amt<=balance:
                balance-=amt
                print("available balance=",balance)

            else:
                print("no funds")
        else:
            print("max withdraw amount is 10000/ only")
    else:
        print("inavlid amount")
else:
    print("invalid pin no")
print("thanks for using ATM")








