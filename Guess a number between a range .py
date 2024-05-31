import random
from_= int(input("Enter a number from:"))
to= int(input("Enter a number to: "))
#We use randint for integer values
a= random.randint(from_,to)
count = 0
print("You only have 10 chances ")
while count<=10:
    guess = int(input("Guess a number: "))
    print(" ")
    if a == guess:
        print("You guessed it right!!!,** Fantastic**")
        break
    elif a > guess:
        count +=1
        print("Guessed number is small")
        print("--Only ",10-count,"chances left--")
    elif a < guess:
        print("Guesses number is big")
        print("--Only ",10-count,"chances left--")
    elif count==10:
        print("Your chances got over, try again")
