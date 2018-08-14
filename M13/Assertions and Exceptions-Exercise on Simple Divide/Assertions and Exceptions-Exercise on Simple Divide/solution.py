'''define the simple_divide function here'''
def simple_divide(item, denom):
    '''start a try-except block'''
    try:
        return item / denom
    except ZeroDivisionError:
        return 0


def fancy_divide(list_of_numbers, index):
    '''fun'''
    denom = list_of_numbers[index]
    return [simple_divide(item, denom) for item in list_of_numbers]


def main():
    '''a'''
    data = input()
    line = data.split()
    line1 = []
    for j in line:
        line1.append(float(j))
    san = input()
    index = int(san)
    print(fancy_divide(line1, index))


if __name__ == "__main__":
    main()
