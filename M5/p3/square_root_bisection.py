'''Write a python program to find the square root of the given number'''
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    '''epsilon and step are initialized
     don't change these values'''
    square = int(input())
    sm_value = 0.01
    num_count = 0
    low = 0
    high = square
    count = (high + low) / 2.0
    while abs(count ** 2 - square) >= sm_value:
        if count ** 2 < square:
            low = count
        else:
            high = count
        count = (high + low) / 2.0
        num_count += 1
    print(count)

if __name__ == "__main__":
    main()
