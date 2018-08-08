'''Exercise : Function and Objects Exercise-3'''
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 16, 64, 81]

def square(number):
    '''returns square of a number'''
    return number*number

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
    apply_to_each(list1, square)

if __name__ == "__main__":
    main()
