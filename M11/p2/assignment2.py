'''Exercise: Assignment-2
Implement the updateHand function. Make sure this function has no side effects: i.e.,
it must not mutate the hand passed in. Before pasting your function definition here,
be sure you've passed the appropriate tests in test_ps4a.py.'''


def updatehand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    newhand = hand.copy()
    for index in word:
        if index in hand:
            newhand[index] = newhand[index] - 1
    return newhand


def main():
    '''a'''
    number = input()
    adict = {}
    for i in range(int(number)):
        data = input()
        space = data.split()
        adict[space[0]] = int(space[1])
    data1 = input()
    print(updatehand(adict, data1))


if __name__ == "__main__":
    main()
