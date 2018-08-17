#This program is used to play truth or dare game and number guessing game
#This program has coin tossing and dice rolling function which can be used to play other games
import random
truth=["Do you ever bunk classes and caught by teacher?","what is you most embarassing story about you?","Do you ever got beaten badly by your parents?","Do you do something unhygenic? If yes what is it?","What was your worst fail ever?","Out of your friends, who do you think is the dumb one?","What is something really stupid you did?","What is the worst mark you ever gotten?","Did you love someone and got rejected?","who is your first crush?"]
dare=["lick your elbow","take a bucket of water and pour it upon you","Computer got bored of thinking and you are escaped"," eat a chilli powder","call someone and prank them","give a chocolate to your enemy"]
coin=["heads","tails"]
dice=["1","2","3","4","5","6"]
dices=["1","2","3","4","5","6","7","8","9","10","11","12"]
guess=["1","2","3","4","5","6","7","8","9","10"]
def truthordare():
    print("Enter truth or dare in lower case")
    choice=(input(""))
    if (choice=="truth"):
        print ('You picked truth.You have to tell...')
        print(random.choice(truth))
    elif(choice=="dare"):
        print ('You picked dare.I dare you to...')
        print(random.choice(dare))
    else:
        print('Trying to cheat?Now you have to play twice and give justice!')
def cointoss():
    print(random.choice(coin))
def rolldice():
    print("Enter 1 or 2 dice:")
    ch=int(input())
    if(ch==1):
        print(random.choice(dice))
    elif(ch==2):
        print(random.choice(dices))
    else:
        print("Enter only 1 or 2 dices")
def guessgame():
    print("Guess the number between 1 to 10:")
    c=int(input())
    if(c==random.choice(guess)):
        print("You wonnn!")
    else:
        print("You loseee!")
#main program starts here
print("Are you got bored? Enjoy playing the following games...")
print("Enter 1.Truth or dare game \n 2.Guessing game \n 3.Tossing coin \n 4.Rolling dice to play")
choices=int(input())
if(choices==1):
    truthordare()
elif(choices==2):
    guessgame()
elif(choices==3):
    cointoss()
elif(choices==4):
    rolldice()
else:
    print("Invalid choice")
print("**Play again**")
    
