'''Matrix operations'''
import copy
def mult_matrix(mtx1, mtx2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    length = len(mtx1)
    if length != len(mtx2[0]):
        print("Error: Matrix shapes invalid for mult")
        return None
    newlist1 = []
    for i in range(0, len(mtx1), 1):
        newlist2 = []
        for j in range(0, len(mtx2[0]), 1):
            result = 0
            for k in range(0, len(mtx2), 1):
                result += int(mtx2[i][k]) * int(mtx2[k][j])
            newlist2.append(result)
        newlist1.append(newlist2)
    return newlist1
def add_matrix(mtx1, mtx2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    length1 = len(mtx1)
    length2 = len(mtx2)
    if length1 != length2:
        print("Error: Matrix shapes invalid for addition")
        return None
    else:
        res = copy.deepcopy(mtx1)
        for i in range(0, length2, 1):
            for j in range(0, len(mtx2[i]), 1):
                res[i][j] = int(res[i][j])
                res[i][j] += int(mtx2[i][j])
        return res

def read_matrix(size):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    rows = int(size[0])
    columns = int(size[1])
    count = 0
    mtx = []
    for _ in range(0, rows, 1):
        row = input().split()
        mtx.append(row)
        count += len(row)
    if count != rows * columns:
        print("Error: Invalid input for the matrix")
    else:
        return mtx

def main():
    '''read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    #multiply matrix 1 and matrix 2'''
    number = input().split(',')
    mtx1 = read_matrix(number)
    number1 = input().split(',')
    mtx2 = read_matrix(number1)
    if mtx1 is None or mtx2 is None:
        return None
    print(add_matrix(mtx1, mtx2))
    print(mult_matrix(mtx1, mtx2))


if __name__ == '__main__':
    main()
