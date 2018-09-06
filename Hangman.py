from random import randint
myWords = ["spaceman", "prism", "trinity", "pasion", "hummus", "wifi", "tablecloth", "picture frame", "painting", "falafel", "scorpion", "rubiks cube", "television", "sunglasses", "slippers", "socks"]

def newWord():
    yesNo = input("Would you like to create your own word or use an existing word? (new/existing) ")
    if yesNo == "new":
        return input("Enter your own word or phrase using only lowercase: ")
    elif yesNo == "existing":
        return myWords[randint(0, len(myWords) -1)]
    else:
        print("Invalid input")
        return newWord()
word = newWord()
wordSplit = list(word)
wordBlanks = []
x = 0
while x < len(wordSplit):
    wordBlanks.append("_")
    x+=1
print(wordSplit)
print(wordBlanks)
indexes = []
guess = " "
def search():
    for index, letter in enumerate(wordSplit):
        if guess == letter:
            indexes.append(index)
            #having trouble here LMKKKK
            return "true"
        else:
            return "false"
    for index in indexes:
        wordBlanks[index] = guess
search()
indexes = []
trials = 0
bool = search()
print(bool)
while wordSplit != wordBlanks:
    guess = input("Guess your letter: ")
    indexes = []
    search()
    print(wordSplit)
    print(wordBlanks)
    if bool != "true":
        trials += 1
        if trials == 1:
            print("You have 5 lives left")
        elif trials == 2:
            print("You have 4 lives left")
        elif trials == 3:
            print("You have 3 lives left")
        elif trials == 4:
            print("You have 2 lives left")
        elif trials == 5:
            print("You have 1 life left")
        else:
            wordSplit = wordBlanks
    indexes = []

if wordSplit == wordBlanks:
    if trials < 6:
        print("Congratulations! You did it!")
    if trials >= 6:
        print("You've failed. Mans is gone")
print(trials)
