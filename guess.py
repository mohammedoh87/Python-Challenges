import random
import time

number = random.randint(1,100)

def intro():
    print("May I ask your name?")
    global name
    name = input()
    print(name + ", we are going to play a game I am thinking of a number between 1 to 100")

    if(number % 2 == 0):
        x = 'even'
    else:
        x = 'odd'
    print("\n This is a {} number".format(x))
    time.sleep(.5)
    print("Go ahead and guess!")

def pick():
    guesses = 0
    while guesses < 6:
        time.sleep(.25)
        enter = input("Guess")

        try:
            guess = int(enter)
            
            if guess <= 100 and guess >= 1:
                guesses = guesses + 1
                if guesses < 6:
                    if guess < number:
                        print("The guess of the number that you entered is too low")
                    if guess > number:
                        print("The guess of the number that you entered is too high")
                    if guess != number:
                        time.sleep(.5)
                        print("Try Again")
                    if guess == number:
                        break
                
            if guess > 100 or guess < 1:
                print("Silly Goose, The number isn't in the range")
                time.sleep(.25)
                print("Please enter a nnumber between 1 and 100")
        
        except:
            print("I don't think that " + enter + "is a number. Sorry")
    
    if guess == number:
        guesses = str(guesses)
        print("Good job, {}!. You guessed the number in {} guesses.".format(name, guesses))
    if guess != number:
        print("Nope, The number I was thinking of was " + str(number))
play_again = "yes"
while play_again == 'yes' or play_again == 'y' or play_again == 'Yes':
    intro()
    pick()
    print("Do you want to play again")
    play_again = input()
    



