'''Exercise: Assignment-2'''
# Write a Python function, sumofdigits, that takes in one number
#and returns the sum of digits of given number.

# This function takes in one number and returns one number.


def sumofdigits(value):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    if value == 0:
        return 0
    return (value % 10) + sumofdigits(int(value // 10))


def main():
    '''this is a program for sum of digits using recursion'''
    number = input()
    print(sumofdigits(int(number)))

if __name__ == "__main__":
    main()
