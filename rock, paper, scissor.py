import random


print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")
while True:
    print("Enter your choice (1 - Rock, 2 - Paper, 3 - Scissors): ")
    player = int(input("Rock, Paper, Scissor?"))
    if player > 3 or player < 1:
        print("Invalid choice, please try again.")

    if player == 1:
        player_choice = "Rock"
    elif player == 2:
        player_choice = "Paper"
    else:
        player_choice = "Scissors"

    print("You chose: " + player_choice)
    computer = random.randint(1, 3)

    if computer == 1:
        computer_choice = "Rock"
    elif computer == 2:
        computer_choice = "Paper"
    else:
        computer_choice = "Scissors"

    print("Computer chose: " + computer_choice)

    print(player_choice + " vs " + computer_choice)

    if player_choice == computer_choice:
       result = "Draw"
    elif (player == 1 and computer == 2) or (player == 2 and computer == 1):
        result = "Paper"
    elif (player == 1 and computer == 3) or (player == 3 and computer == 1):
        result = "Rock"
    elif (player == 3 and computer == 2) or (player == 2 and computer == 3):
        result = "Scissors"

    if result == "Draw":
        print("It's a tie!")
    elif result == player_choice:
        print("You win!")
    else:
        print("You lose!")

    print("Do you want to play again? (y/n)")
    again = input().lower()
    if again == "n":
        break
    elif again != "y" and again != "n":
        print("Invalid choice, please try again.")

print("Thanks for playing!")

