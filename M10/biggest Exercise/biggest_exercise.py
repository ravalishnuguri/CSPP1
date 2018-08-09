'''Exercise : Biggest Exercise'''
#Write a procedure, called biggest, which returns the key corresponding
#to the entry with the largest number of values associated with it.
#If there is more than one such entry, return any one of the matching keys.


def biggest(beings):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    values = beings.values()
    count = 0
    for j in values:
        if len(j)>count:
            count = len(j)
    for i in beings:
        c = len(beings[i])
        if c==count:
            return i
            break




def main():
    '''dict'''
    number = input()
    animals = {}
    for i in range(int(number)):
        entries = input()
        list1 = entries.split()
        if list1[0][0] not in animals:
            animals[list1[0][0]] = [list1[1]]
        else:
            animals[list1[0][0]].append(list1[1])
    print(animals)
    print(biggest(animals))

    #animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

    #animals['d'] = ['donkey']
    #animals['d'].append('dog')
    #animals['d'].append('dingo')
    #print(animals)
    #print(biggest(animals))


if __name__ == "__main__":
    main()
