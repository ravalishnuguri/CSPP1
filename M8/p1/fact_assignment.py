'''Exercise: Assignment-1'''
# Write a Python function, factorial(n), that takes in
#one number and returns the factorial of given number.

# This function takes in one number and returns one number.


def factorial(value):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if value == 1:
        return 1
    return value*factorial(value-1)



def main():
    '''this is a factorial recursion program'''
    number = input()
    print(factorial(int(number)))

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(25500)
    main()
