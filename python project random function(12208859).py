from random import *
import os
print("Welcome to the number guessing game")
print("Follow the instruction please and do as directed timely")
print("you will get score added by 5 if you got the right number")

#print(randomnumberbypc)
score=0
win=0
loose=0
totalmatch=0
playagaingame="YES"
while playagaingame=="YES":
    totalmatch=totalmatch+1
    lower=int(input("Enter the lower bound:     "))
    upper=int(input("Enter the upper bound:     "))
    randomnumberbypc=randint(lower,upper-1)
    for i in range(0,3):
        choice=int(input("Enter your choice:   "))
        if choice==randomnumberbypc:
            print("Right number guessed")
            print("You win")
            score=score+5
            #print("Your score is",score)
            break
        elif choice>randomnumberbypc:
            print("Your guess was too high")
            print("Have one more try")
            score=score+0
        elif choice<randomnumberbypc:
            print("Your guess was too low")
            print("Have one more try")
            score=score+0


    print("Your score is",score)
    playagain=str(input("You want to play again(YES/NO):    "))
    playagaingame=playagain.upper()

print("Your final score is    ",score)
print("Total number of match:   ",totalmatch)
win=score/5
print("Total number of win are:     ",win)
loose=totalmatch-win
print("Total number of loose are:    ",loose)
accuracy=(win/totalmatch)*100
print("Your accuracy is:    ",accuracy)

print("Thanks for playing")
print("Hope you have enjoyed the game")
