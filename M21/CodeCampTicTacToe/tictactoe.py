def wincheck(row):
    new1 = set()
    new2 = set()
    new3 = set()
    for i in range(len(row)):
        for j in range(len(row[i])):
            if i == j:
                new1.add(row[i][j])
            if i + j == len(row) - 1:
                new2.add(row[i][j])
    if len(new1) == 1:
        if 'x' in new1:
            return x
        return o
    if len(new2) == 1:
        if 'x' in new2:
            return x
        return o


def gamerules(row):
    for i in row:
        len(i) != 3
        return "invalid game"
    countofx = index.count("x")
    countofo = index.count("o")
    countofdot = index.count(".")
    if sum(countofx + countofo + countofdot) != 9:
        return "invalid input"
    if abs(countofx - countofo) != 1:
        return "invalid game"



def main():
    '''main function for the tic-tac-toe game'''
    row = []
    for i in range(3):
        matrix = input()
        matrix = list(map(str, matrix.split()))
        row.append(matrix)
    # print(row)
    print(gamerules(row))
    print(wincheck(row))



if __name__ == '__main__':
    main()
