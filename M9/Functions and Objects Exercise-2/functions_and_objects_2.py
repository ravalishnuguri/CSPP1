'''Exercise : Function and Objects Exercise-2'''
#Implement a function that converts the given testList = [1, -4, 8, -9] into [2, -3, 9, -8]

def inc(number):
    '''it is a increment function'''
    return number+1

def apply_to_each(listss, func):
    '''it is a mapping function'''

    print(list(map(func, listss)))


def main():
    '''list'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    apply_to_each(list1, inc)

if __name__ == "__main__":
    main()
