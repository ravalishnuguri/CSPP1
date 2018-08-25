'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    '''function for cleaning a string'''
    newstring = string.lower().strip()
    newstring1 = re.sub('[^a-z0-9]', '', newstring)
    newstring1
    newstring2 = re.sub(r"\s+", "", newstring1,)
    return newstring2

def main():
    '''f
    '''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
