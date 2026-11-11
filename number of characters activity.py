word = input("Enter your word:")
character = input("Enter your character:")
count=0
for c in word:
    if character == c:
     count+=1
print("Count:", count)
