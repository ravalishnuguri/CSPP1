'''Write a python program to find the square root of the given number'''
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    ''' epsilon and step are initialized'''
    # don't change these values
    square = int(input())
    epsilon = 0.01
    # your code starts here
    guess = square / 2.0
    num_guesses = 0
    while abs(guess * guess - square) >= epsilon:
        num_guesses += 1
        guess = guess - (((guess ** 2) - square) / (2 * guess))
    print(str(guess))

if __name__ == "__main__":
    main()
