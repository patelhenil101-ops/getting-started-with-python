def shutdown(answer):
    if answer == "Yes":
        print("Shutting down")
    elif answer == "no":
        print("Abort shut down")
    else:
        print("Sorry")

shutdown(input("Enter Yes or no: "))