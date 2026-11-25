try:
    age = int(input("Enter your age: "))

except ValueError:
    print("Value error")

else:
    if age % 2 == 0:
        print("Even")
    else:
        print("Odd")