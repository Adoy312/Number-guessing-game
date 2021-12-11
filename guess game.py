import random

a = int(input("Enter where to start the range: "))
b = int(input("Enter where to end the range: "))

print("Your selected range is " + str(a) + "-" +str(b))

rand = random.randint(int(a), int(b))
print("You have only five guesses!")
count = 0
guess=""

while count < 5:
    guess = input("Guess the random integer: ")
    guess = int(guess)
    
    if guess == rand:
        print("Congrats,u made it!")
        break
    
    elif guess< rand:
        print("Try Again! You guessed too small")
        
    elif guess > rand :
        print("Try Again! You guessed too high")
        
    count= count +1



    
if count == 5 and guess!=rand:
    print("Oops you are outta guesses!!! ")
    print("The random integer is "+ str(rand))
    print("Better luck next time.")
    
elif count ==5 and guess == rand:
    print("You made it in the nick of time.")
