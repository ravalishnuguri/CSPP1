'''
Given a  number int_input, find the product of all the digits
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    number = int(input())
    sum1 = 1
    count = 1
    if number < 0:
        number = -number
    elif number == 0:
        sum1 = 0
    while number != 0:
        if number == 0:
            count = 1
        else:
            msit = number % 10
            sum1 = sum1 * msit
            number = number // 10
            count = 0
    if count == 0:
        print(sum1)
    else:
        print("0")

if __name__ == "__main__":
    main()
