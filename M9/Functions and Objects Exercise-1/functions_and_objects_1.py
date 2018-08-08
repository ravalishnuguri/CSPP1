'''Exercise : Function and Objects Exercise-1'''
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 4, 8, 9]


def apply_to_each(listss, func):
    '''Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 4, 8, 9]'''
    print(list(map(func, listss)))


def main():
    '''list'''
    numoflist = input()
    numoflist = numoflist.split()
    list1 = []

    for j in numoflist:
        list1.append(int(j))
    apply_to_each(list1, abs)

if __name__ == "__main__":
    main()
