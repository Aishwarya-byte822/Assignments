import random

choices = ["rock", "paper", "scissor"]

user_score = 0
computer_score = 0

for i in range(5):

    computer = random.choice(choices)

    n = input("\nEnter rock, paper, scissor: ")

    if n not in choices:
        print("Invalid choice!")
        continue

    print(f"You choose: {n}")
    print(f"Computer choose: {computer}")

    if n == computer:
        print("It's a draw")
        user_score += 1
        computer_score += 1

    elif (
        (n == "rock" and computer == "scissor") or
        (n == "paper" and computer == "rock") or
        (n == "scissor" and computer == "paper")
    ):

        print("You won!")
        user_score += 2

    else:
        print("You lose! Computer wins")
        computer_score += 2

    print("Your Score:", user_score)
    print("Computer Score:", computer_score)

print("\nFinal Result")

if user_score > computer_score:
    print("You won the game!")

elif computer_score > user_score:
    print("Computer won the game!")

else:
    print("Game draw!")