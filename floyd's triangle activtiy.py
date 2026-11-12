rows = int(input("Enter the number of rows:"))
count = 1
for c in range(rows):
    for d in range(c+1):
        print(count, end=" ")
        count+=1
    print()