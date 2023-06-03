def Finished():
    task_done = input ("When you are finished reading, please press enter to end program.")


player1 = input ("Please state your name player 1: ")


while True:
    if any (char.isdigit() for char in player1):
        print ("Please do not include digits in your name.")
        player1 = input ("Please state your name player 1: ")
    else:
        break


player2 = input ("Player 2, please state your name: ")


while True:
    if any (char.isdigit() for char in player2):
        print ("Please do not include digits in your name.")
        player2 = input("Player 2, please state your name: ")
    elif player2 == player1:
        print("Choose different names.")
        player2 = input("Player 2, please state your name: ")
    else:
        break


print ("Welcome ", player1, " and ", player2, " let's begin the game!")

player1InputAttempt = 1
player2InputAttempt = 1

while True:
    player1Input = input(player1 + " please choose one of the 3 listed options: rock, paper or scissors: ")
    if player1Input.lower == "rock" or "scissors" or "paper":
        break
    else:
        print("Please type in the options with a lower or upper case. ")
#The counter is simply there for fun and exploring different ways to implement things within code.
        print("You're currently at attempt: ", player1InputAttempt)
        player1InputAttempt = player1InputAttempt + 1

while True:
    player2Input = input(player2 + " please choose one of the 3 listed options: rock, paper or scissors: ")
    if player2Input.lower == "rock" or "scissors" or "paper":
        break
    else:
        print("Please type in the options with a lower or upper case. ")
        print("You're currently at attempt: ", player2InputAttempt)
        player2InputAttempt = player2InputAttempt + 1


'''
Basic psuedo code of outputs
if player 1 == player 2 draw

if player 2 = rock and player 1 = scissors
player 2 Win

if player 2 = scissors and player 1 = paper
player 2 win

if player 2 = paper and player 1 = rock
player 2 Win

else player 1 wins
'''


if player1Input == player2Input:
    print("It was a draw!")

elif player2Input == "rock" and player1Input == "scissors":
    print("Player 2 wins!")

elif player2Input == "scissors" and player1Input == "paper":
    print("Player 2 wins!")

elif player2Input == "paper" and player1Input == "rock":
    print("Player 2 wins!")

else:
    print("Player 1 wins!")

print("Thank you for playing! I hope you play again.")
Finished()










