import random
playing = True
number = str(random.randint (0,9))

print("I will choose a random number from 0 to 9 and you will have to try and guess it.")
while playing:
    guess = str(input("Enter your guess:"))
    if number == guess:
        print("You win!")
        break
    else:
        print("Your guess is incorrect try again")