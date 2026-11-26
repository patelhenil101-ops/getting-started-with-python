import random
while True:
    user_action = input(" Enter a choice Rock, Paper or Scissor")
    possible_action = ["Rock", "Paper", "Scissor"]
    computer_action = (random.choice(possible_action))
    print(f"\nYou choose {user_action}, computer chose {computer_action}")

    if user_action == computer_action:
        print("You tied")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("You win rock smashes scissors")
        else:
            print("Paper covers rock, You lose")

       
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")

    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    #take input for playing again
    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break
