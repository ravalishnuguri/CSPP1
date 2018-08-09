'''Exercise : how many'''
# write a procedure, called how_many, which returns the
#sum of the number of values associated with a dictionary.


def how_many(animals):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    sum1 = 0
    values = animals.values()
    for words in values:
        sum1 = sum1 + len(words)
    return sum1

def main():
    '''dist'''
    number = input()
    animals = {}
    for i in range(int(number)):
        entries = input()
        list1 = entries.split()
        if list1[0][0] not in animals:
            animals[list1[0][0]] = [list1[1]]
        else:
            animals[list1[0][0]].append(list1[1])
    #animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

    #animals['d'] = ['donkey']
    #animals['d'].append('dog')
    #animals['d'].append('dingo')
    print(animals)
    print(how_many(animals))


if __name__ == "__main__":
    main()
