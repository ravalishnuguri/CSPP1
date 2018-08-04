'''
Given a  number int_input, find the product of all the digits
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    number = int(input())
    sum1 = 1
    while number != 0:
        msit = number % 10
        sum1 = sum1 * msit
        number = number // 10
    if number == 0:
        print("0")
    else:
        print(sum1)

if __name__ == "__main__":
    main()
