import random
while True:
    user_action = input(" Enter a choice Rock, Paper or Scissor")
    possible_action = ["Rock", "Paper", "Scissor"]
    computer_action = (random.choice(possible_action))
    print(f"\nYou choose {user_action}, computer chose {computer_action}")

    if user_action == computer_action:
        print("You tied")
    elif computer_action == "rock":
        if computer_action == "scissors":
            print("You lose rock smashes scissors")
        else:
            print("Paper covers rock, You lose")

             computer_action == "paper":

