'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    # '''
    # for index in range(0, len(sudoku), 1):
    #     for j in range(0, len(sudoku[index]), 1):
    #         # new = sudoku[index[j]]
    #         if sudoku[index[j]] >= 0 and sudoku[index[j]] <= 9:
    #             return True
    return False

def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    # initialize empty list
    sudoku = []


    # loop to read 9 lines of input from console
    for _ in range(9):
        # read a line, split it on SPACE and append row to list
        row = list(map(int, input().split(' ')))
        sudoku.append(row)
    # call solution function and print result to console
    # print(sudoku)
    # print(int(sudoku[5][6]))
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()
