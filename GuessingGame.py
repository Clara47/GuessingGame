#The goal of this program is to create a guessing game between two players.
#input
print("I have a number between 1 and 10 in my head.")
print("Take turns trying to guess which number I'm thinking of, but first, I need your names.")
player1=input("Player 1, what's your name?")
player2=input("Player 2, what's your name?")
guess=0
guessCount=0
roundCount=0
player1wins=0
player2wins=0

while roundCount<3:
    roundCount=roundCount+1
    print("You are beginning a new round!")
    import random 
    correct = random.randrange(1,10)
    #print(str(correct))
    guessCount=0
    while guess!=correct and guessCount<10:
        guessCount=guessCount+1
        if guessCount%2==0:
            #player2
            guess=int(input(str(player2)+(" enter your number:")))
        else:
            #player1
            guess=int(input(str(player1)+(" enter your number:")))
            
        if guessCount==10:
            print("You ran out of tries!")
            print("You lose "+ str(player1)+ " and " +str(player2)+"!!")
        elif guess==correct:
            print("Victory! You win this round!")
        elif guess>10 or guess<1:
            print("Invalid guess: Choose numbers BETWEEN 1 and 10.")
            guess=int(input("Try again? Enter your number:"))
        elif guess>correct:
            print("Your guess is too high!")
        else:
            print("Your guess is too low!")
            
        if guessCount<10 and guess==correct and guessCount%2==0:
            print("Great job "+ str(player2)+"!")
            player2wins=player2wins+1
        elif guessCount<10 and guess==correct:
            print("Great job "+ str(player1)+"!")
            player1wins=player1wins+1
        else:
            print("Try again!")
            
print("You won "+str(player1wins)+" times, " + str(player1))
print("You won "+str(player2wins)+" times, " + str(player2))
if player1wins>player2wins:
    print("You are the ultimate winner, " +str(player1)+"!")
elif player2wins>player1wins:
    print("You win, "+str(player2)+"!")
else:
    print("You both are such losers.")
        
               
        
