#Finished function for keeping terminal open during usage of users.
def Finished():
    task_done = input ("When you are finished reading, please press enter to end program.")


player1 = input ("Please state your name player 1: ")

#input validation of no digits within the names. Symbols skipped over due to limitation of knowledge at time of coding. 
while True:
    if any (char.isdigit() for char in player1):
        print ("Please do not include digits in your name.")
        player1 = input ("Please state your name player 1: ")
    else:
        break


player2 = input ("Player 2, please state your name: ")

#input validation of no digits within the names. A double up on names results in a retry of name input.
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

#player attempt counting for fun
player1InputAttempt = 1
player2InputAttempt = 1

acceptableInput = ["rock", "scissors", "paper", "Rock", "Scissors", "Paper"]


player1Input = input(player1 + "," + " please choose one of the 3 listed options: rock, paper or scissors: ")

#doubled up with no function due to limitations of knowledge when this code was written, kept and not upgraded for future reference of knowledge.
#verification for 
# #The counter is simply there for fun and exploring different ways to implement things within code.
while True:
    if player1Input in acceptableInput:
        break
    else:
        print("Please type in the options with a lower or upper case. ")
        print("You're currently at attempt: ", player1InputAttempt)
        player1InputAttempt = player1InputAttempt + 1
        player1Input = input(player1 + "Please choose one of the choices; rock, paper or scissors:")



player2Input = input(player2 + "," + " please choose one of the 3 listed options: rock, paper or scissors: ")

#repeat for player 2 verification.
while True:
    if player2Input in acceptableInput:
        break
    else:
        print("Please type in the options with a lower or upper case. ")
        print("You're currently at attempt: ", player2InputAttempt)
        player2InputAttempt = player2InputAttempt + 1
        player2Input = input(player2 + "Please choose one of the choices; rock, paper or scissors:")

player1Input = player1Input.lower()
player2Input = player2Input.lower()
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

#checking for a draw before going into winning scenarios
if player1Input == player2Input:
    print("It was a draw!")
#All player 2 winning scnarios with a default of player 1 wins after.
elif player2Input == "rock" and player1Input != "paper":
    print("Player 2 wins!")

elif player2Input == "scissors" and player1Input != "rock":
    print("Player 2 wins!")

elif player2Input == "paper" and player1Input != "scissors":
    print("Player 2 wins!")
    
else:
    print("Player 1 wins!")

print(player1, "Chose:", player1Input)

print(player2, "Chose:", player2Input)

print("Thank you for playing!")
Finished()










