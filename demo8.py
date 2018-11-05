tm=float(input("enter total marks:"))
if tm>360:
    print("First class")
elif tm>=300 and tm<360:
    print("second class")
elif tm<300:
    print("third class")
else:
    print("invalid")


print("thanks")