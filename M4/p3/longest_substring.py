'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in
which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem,
we suggest that you move on to a different part of the course.
If you have time, come back to this problem after
you've had a break and cleared your head.'''

def main():
    '''alphabetical sequence'''
    str1 = input()
    # the input string is in s
    # remove pass and start your code here
    count = 0
    j = 0
    k = 0
    str2 = ""
    for i in range(0, len(str1)-1, 1):
        if str1[i] <= str1[i+1]:
            count += 1
        else:
            count = 0
        if j < count:
            j = count
            k = i
    str2 = k-j+1
    print(str1[str2:str2+j+1])

if __name__ == "__main__":
    main()
