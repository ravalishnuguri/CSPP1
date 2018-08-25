'''
Write a python program to read multiple lines of text input and store the input into a string.
'''
def newlines(newline):
    '''printing new line'''
    newl = newline
    return newl

def main():
    '''f
    '''
    documents = ""
    lines = int(input())
    for i in range(lines):
        i += 1
        documents += input()
        documents += '\n'
    print(newlines(documents))


if __name__ == '__main__':
    main()
