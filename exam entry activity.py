medical=input("Did, you have a medical emergency, press 'y' for yes and 'n' for no.")
if medical=='y':
    print("You are allowed.")
else:
    attendance=int(input("Enter your attendance percentage:"))
    if attendance >75:
        print("You are allowed")
    else:
        print("You are not allowed")