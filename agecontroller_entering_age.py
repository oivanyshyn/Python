age=input ("please enter your age: ")
if not age.isnumeric():
    print ("Enter a number")
elif age:
    age=int(age)
    if age>=19:
        print ("You are good to go")
    elif age<19:
        print("Sorry you ate too young")
else:
    print ("You entered nothing")

