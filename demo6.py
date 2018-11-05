name=input("plz enter your name:")
designation=input("plz enter your designation in small letter only:")
salary=float(input("plz enter your salary:"))
if designation=="manager":
    bonous= salary*20/100
    print("hello",name+" your salary is:",bonous+salary)
elif designation=="clerk":
    bonous= salary*5/100
    print("hello", name + " your salary is:", bonous + salary)
elif designation=="analyst":
    bonous= salary*10/100
    print("hello", name + " your salary is:", bonous + salary)
else:
    print("something gone wrong plz try again")
print("thanks")

