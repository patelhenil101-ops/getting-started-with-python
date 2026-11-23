def calculate_change(bill, paid):
    change = paid - bill 
    return change
bill = int(input("Enter the amount of bill"))
paid = int(input("Enter  the amount you paid"))
answer = calculate_change(bill, paid)
print("The amount of change is:", answer)