answer= input ("choose from [apple, grape, bacon, fish, carrot]: ").lower
if answer== "apple" or answer=="grape":
    print ("Fruit")
elif answer == "bacone" or answer== "fish":
    print ("meat")
elif answer=="carrot":
    print ("vegetable")
else:
    print ("choose only one from this list[apple, grape, bacon, fish, carrot]")