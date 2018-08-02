'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example,
if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
    '''program to find bob string'''
    str1 = input()
    # the input string is in s
    # remove pass and start your code here
    count = 0
    i = str1.find("bob")
    while i >= 0:
        count += 1
        i = str1.find("bob", i+2)
    print(count)
if __name__ == "__main__":
    main()
