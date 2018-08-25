'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
import collections
def tokenize(string):
	'''we are counting the number of words in the string'''
	newtext = ""
	newtext = "".join(string)
	newtext = newtext.lower()
	# newstring1 = re.sub('[^a-z]', '', newtext)
	newstring1 = re.sub('[^a-zA-Z]', '', newtext)
	# print(newstring1)
	freq1 = {}
	freq1 = collections.Counter(newstring1)
	print(freq1)
    
            
def main():
    '''
        main function
    '''
    document = []
    lines = int(input())
    for i in range(lines):
    	document.append(input())
    	i += 1
    # print(document)
    tokenize(document)

if __name__ == '__main__':
    main()
