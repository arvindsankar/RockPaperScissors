import random

def correct_input(choice):
	
	while choice != "Rock" and choice != "Scissors" and choice != "Paper":

		# corrects rock
		if choice == "rock" or choice == "R" or choice == "r":
			choice = "Rock"

		# corrects scissors
		elif choice == "scissors" or choice == "S" or choice == "s":
			choice = "Scissors"

		# corrects paper
		elif choice == "paper" or choice == "P" or choice == "p":
			choice = "Paper"

		else:
			print ("Sorry, didn't get that.\n")
			choice = input("Do you chose Rock, Paper, or Scissors? ")
	return choice		

print ("\nTo play, select one of the following choices: Rock, Paper, or Scissors.\n")

print ("Rock beats Scissors and loses to Paper.")
print ("Paper beats Rock and loses to Scissors")
print ("Scissors beats Paper and loses to Rock\n")

# prompt player for choice
choice = input("Do you chose Rock, Paper, or Scissors? ")
choice = correct_input(choice)

# CPU randomly selects from this list of choices
CPUChoices = ["Rock", "Paper", "Scissors"]

# CPU
CPU = CPUChoices[random.randrange(0,3)]

while choice == CPU:
	print ("You and the Computer both picked " + CPU + " so we'll try again.\n")
	choice = input("Do you chose Rock, Paper, or Scissors? ")
	choice = correct_input(choice)
	CPU = CPUChoices[random.randrange(0,3)]

print ("\nYou chose: " + choice)
print ("Computer choses: " + CPU + "\n")  

# Player choses Rock
if (	choice == "Rock" and CPU == "Paper"
	or 	choice == "Paper" and CPU == "Scissors"
	or  choice == "Scissors" and CPU == "Rock"
	):
   	print (CPU + " beats " + choice + ". You lose!")
else:
	print (choice + " beats " + CPU + ". You win!")
print ("\nThanks for playing!")
