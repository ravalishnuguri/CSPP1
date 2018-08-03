'''Write a python program to find the square root of the given number'''
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    ''' epsilon and step are initialized
     don't change these value
     your code starts here'''
    square = int(input())
    sm_value = 0.01
    count = 0.0
    i = 0.1
    num_count = 0
    while abs(count ** 2 - square) >= sm_value:
        count += i
        num_count += 1
    if abs(count ** 2 - square) >= sm_value:
        print(square)
    else:
        print(count)

if __name__ == "__main__":
    main()
