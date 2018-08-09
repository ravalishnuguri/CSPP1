'''Hangman game'''
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadwords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseword(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadwords()

def iswordguessed(secretword, lettersguessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count1 = 0
    for index in secretword:
        if index in lettersguessed:
            count1 += 1
    return bool(count1 == len(secretword))



def getguessedword(secretword, lettersguessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    new = ""
    length = len(secretword)
    for letter in range(length):
        if secretword[letter] in lettersguessed:
            new += secretword[letter]
        else:
            new += '_'
    return new



def getavailableletters(lettersguessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    newalphabets = ""
    newalphabets = [index2 for index2 in alphabets if index2 not in lettersguessed]
    return "".join(newalphabets)



def isinputcorrect(guess):
    if len(guess) > 1 or (guess <= 'a' and guess >= 'z'):
        print("invalid input")
        return False
    return True


def hangman(secretword):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!!!")
    lettersguessed = []
    print("i am thinking of a word that is", len(secretword), "letters long")
    print("------------")
    flag = False
    maxguessletters = len(secretword)+5
    while maxguessletters != 0:
        print("you have", maxguessletters, " guesses left")
        print("Available Letters: ", getavailableletters(lettersguessed))
        guess = input("please guess a letter: ")
        maxguessletters -= 1
        if not isinputcorrect(guess):
            continue
        lettersguessed.append(guess)
        flag = iswordguessed(secretword, lettersguessed)
        if flag:
            break
        print(getguessedword(secretword, lettersguessed))

    if flag:
        print("congratulations....")
    else:
        print("try again with a new secretword")
        print("the secretword was:", secretword)







# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretword = chooseword(wordlist).lower()
hangman(secretword)
