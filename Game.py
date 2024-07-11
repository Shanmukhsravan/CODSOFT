import random

options = ("rock", "paper", "scissors")
running = True
user_score = 0
computer_score = 0

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
        user_score += 1
    elif player == "paper" and computer == "rock":
        print("You win!")
        user_score += 1
    elif player == "scissors" and computer == "paper":
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

    print(f"Score - You: {user_score}, Computer: {computer_score}")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")
print(f"Final Score - You: {user_score}, Computer: {computer_score}")
