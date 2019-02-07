import random
import sys

def Lives(Incorrect):
    LivesLeft = IncorrectLimit - Incorrect
    print("You have", LivesLeft, "lives left.")

def Hint(Incorrect, WordChoice):
    if Incorrect == 6:
        WordChoice = list(WordChoice)
        WordHint = random.choice(WordChoice)
        WordChoice = "".join(WordChoice)
        print("Hint - the word contains the letter: ", WordHint)

List1 = ["fable","surf","english","paris","flower","laptop","sand","classroom", "blonde", "star", "blue", "hat", "snow", "tennis", "gate", "palm","internet","bricks", "bird", "mountain", "crate", "jumper", "whiteboard", "teacher", "table", "paving", "vehicle", "roundabout", "grass", "window", "cat", "dog", "bag", "bycicle", "jewellery", "headphones"] #These are all the words that can possibly be taken
IncorrectLimit = 7
times = 99
Incorrect = 0
List2 = []

input("Press \"Enter\" to start a game." + "\n")

for i in range(times):
    WordChoice = (random.choice(List1))
    LetterCount = len(WordChoice)
    print("-----NEW GAME-----\n")
    print("The word is", LetterCount, "letters long.")
    if LetterCount == 1:
        L = ("_")
        print(L.replace("", " ")[1: -1], "\n")
    if LetterCount == 2:
        L = ("__")
        print(L.replace("", " ")[1: -1], "\n")
    if LetterCount == 3:
        L = ("___")
        print(L.replace("", " ")[1: -1], "\n")
    if LetterCount == 4:
        L = ("____")
        print(L.replace("", " ")[1: -1], "\n")
    if LetterCount == 5:
        L = ("_____")
        print(L.replace("", " ")[1: -1], "\n")
    if LetterCount == 6:
        L = ("______")
        print(L.replace("", " ")[1: -1], "\n")
    if LetterCount == 7:
        L = ("_______")
        print(L.replace("", " ")[1: -1], "\n")
    if LetterCount == 8:
        L = ("________")
        print(L.replace("", " ")[1: -1], "\n")
    if LetterCount == 9:
        L = ("_________")
        print(L.replace("", " ")[1: -1], "\n")
    if LetterCount == 10:
        L = ("__________")
        print(L.replace("", " ")[1: -1], "\n")

    GuessList = list(L)
    LivesLeft = IncorrectLimit - Incorrect

    for i in range(times):
        if GuessList == WordChoice:
            break

        Hint(Incorrect, WordChoice)

        for i in range(times):
            Guess1 = input("Guess a letter: ")
            GuessLength = len(Guess1)
            if GuessLength > 1:
                print("Please enter only one letter.")
            elif Guess1 == "":
                print("Please enter a letter.")
            else:
                break

        Guess1 = Guess1.lower()
        List2.append(Guess1)

        if WordChoice.find(Guess1) >= 0:
            GuessList = list(GuessList)
            for x, y in enumerate(WordChoice):
                if Guess1 == y:
                    GuessList[x] = y
            print("The letter", Guess1.upper(), "was correct.")
            GuessList = "".join(GuessList)

        else:
            Incorrect += 1
            print("Incorrect.")
            GuessList = "".join(GuessList)
            Lives(Incorrect)

        List2 = "".join(List2)
        print("Guessed Letters: ",List2.upper())
        List2 = list(List2)
        List2.append(", ")
        print(GuessList.replace("", " ")[1: -1], "\n")

        if GuessList == WordChoice:
            print("Well done, you guessed the correct word!")
            Incorrect = 0
            List2 = []
            GuessList = []
            sys.exit()

        if Incorrect == 7:
            print("Game over.")
            print("The word was: ", WordChoice )
            Incorrect = 0
            List2 = []
            GuessList = []
            sys.exit()