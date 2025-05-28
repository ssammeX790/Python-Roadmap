from random import *

while True:
    #Select Difficulty
    print("Select Difficulty")
    print("1. Easy = (15 guesses)")
    print("2. Medium = (8 guesses)")
    print("3. Hard (5 guesses)")
    print("")


    difficulty = input("Enter your choise: ")
    if difficulty in("1", "2", "3"):
        pass
    else:
        print("Thats not even an option dumbass. You are not allowd to play")
        break
    difficulty = int(difficulty)
    print("")

    if difficulty == 1:
        print("Great! you went for the easy difficulty level")
    elif difficulty == 2:
        print("Great! you went for the medium difficulty level")
    elif difficulty == 3:
        print("Okay, you think you can handle the hard difficulty")
    print("")
    print("Let the game begin")

    guessesLeft = 0
    if difficulty == 1:
        guessesLeft = 15
    elif difficulty == 2:
        guessesLeft = 8
    elif difficulty == 3:
        guessesLeft = 5
    print("Guesses left = ", guessesLeft)

    lanumero = randrange(1,100)
    while guessesLeft > 0:
        print(lanumero)

        guess = int(input("Guess the Number: "))

        if guess < lanumero:
            print("Thats low bro")
            guessesLeft -=1
            print("You have ", guessesLeft, " guesses left")
        elif guess > lanumero:
            print("That is to high")
            guessesLeft -=1
            print("You have ", guessesLeft, " guesses left")
        elif guess == 69:
            print("You have found the holy grail, you shall recive 1500 guesses")
            print("No way you fuck this up")
        else:
            print("That is correctly guesst and you have won with ",guessesLeft," guesses left!!")
            break

    if guessesLeft == 0:
        print("You are one again a dissapointment and are no longer allowd to play")
        if input("Kidding, I need the attention. Do you want to play again? ") == "yes" or "Yes" or "YES" or "ok" or "fine" or "if i really have to":
            pass
        else:
            break
    else:
        if input("You know your stuff. Want to do it again? ") == "yes" or "Yes" or "YES" or "ok" or "fine" or "if i really have to":
            pass
        else:
            break
