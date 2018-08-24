'''tic-tac-toe game'''
def loop(seti):
    '''checking value of elements in a set'''
    if 'x' in seti:
        return 'x'
    return 'o'


def wincheck(game):
    '''checking the game rules for winner'''
    new1 = set()
    new2 = set()
    new3 = set()
    new4 = set()
    new5 = set()
    length = len(game)
    for i in range(length):
        for j in range(len(game[i])):
            if i == j:
                new1.add(game[i][j])
            if i + j == (len(game) - 1):
                new2.add(game[i][j])
            newt = set(game[i])
            if len(newt) == 1:
                if 'x' in newt:
                    return 'x'
                return "o"
            if j == 0:
                new3.add(game[i][j])
            if j == 1:
                new4.add(game[i][j])
            if j == 2:
                new5.add(game[i][j])
    if len(new1) == 1:
        return loop(new1)
    if len(new2) == 1:
        return loop(new2)
    if len(new3) == 1:
        return loop(new3)
    if len(new4) == 1:
        return loop(new4)
    if len(new5) == 1:
        return loop(new5)
    return "draw"

def gamerules(row):
    '''checking if the given input is right or wrong'''
    palyer1 = 'x'
    player2 = 'o'
    countofx = 0
    countofo = 0
    countofdot = 0
    for index in row:
        if len(index) != 3:
            return "invalid game"
        if palyer1 in index:
            countofx += index.count(palyer1)
        if player2 in index:
            countofo = index.count(player2)
        if '.' in index:
            countofdot = index.count('.')
    if countofx + countofo + countofdot != 9:
        return "invalid input"
    if abs(countofx - countofo) != 1:
        return "invalid game"
    return wincheck(row)



def main():
    '''main function for the tic-tac-toe game'''
    row = []
    for _ in range(3):
        matrix = input()
        matrix = list(map(str, matrix.split(' ')))
        row.append(matrix)
    # print(row)
    print(gamerules(row)



if __name__ == '__main__':
    main()
