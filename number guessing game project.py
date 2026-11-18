secret=47
print("You have 5 guesses to guess the secret number mfro 1 to 50")

for i in range(5):
  answer=int(input("enter your guess:"))
  if answer > secret:
    difference = answer - secret
  else:
    difference = secret - answer
    if difference > 30:
      print("Ice cold")
    elif difference > 20:
      print("cold")
    elif difference > 10:
      print("Warm")
    else:
      print("Hot")

if answer==secret:
    print("You won!")
else:
    print("Better luck next time")
