import random

def mastermind(secret):
    player = str(input("Try to guess the 4 digit number: "))
    if len(player) != 4:
        player = str(input("Try to guess the 4 digit number: "))
    attempts = 1
    if player == secret:
        print('You are a Mastermind!')
    else:
        while (player != secret):
            guessed = []
            for i in range(4):
                if player[i] == secret[i]:
                    guessed.append(secret[i])
                else:
                    guessed.append("X")
            print(" ".join(guessed))

            player = str(input("Try to guess the 4 digit number: "))
            attempts += 1

            if player == secret:
                print(f'You guessed the correct number in {attempts} attempts!')
                break
    return attempts


player_1 = str(random.randrange(1000, 10000))
score_1 = mastermind(player_1)
print(score_1)
player_2 = str(random.randrange(1000, 10000))
score_2 = mastermind(player_2)
print(score_2)


if score_1 == score_2:
    print("It's a tie! Play again!")
elif score_1 <= score_2:
    print("Player 1 wins!")
else:
    print("Player 2 wins!")







