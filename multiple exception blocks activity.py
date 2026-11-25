try:
    num1, num2 = eval(input("Enter two numbers seperated by commas:"))
    result = num1/num2

except ZeroDivisionError:
    print("Dividing by zero is an error")

except SyntaxError:
    print("Comma is missing. Enter numbers seperated by commas like this 1,2")

except:
    print("Wrong input")
else:
    print("No exceptions")

finally:
    print("This will execute no matter what")