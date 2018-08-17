'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math
import collections

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    new1 = dict1.lower()
    new2 = dict2.lower()

    # str1 = re.sub(r'[^a-z]', '', dict1).split()
    # str2 = re.sub(r'[^a-z]', '', dict2).split()
    str1 = re.sub(r'[^a-zA-Z ]', '',  new1).strip().split()
    str2 = re.sub(r'[^a-zA-Z ]', '',  new2).strip().split()
    # str1 = re.sub(r'^[0-9]+', '', string1)
    # str2 = re.sub(r'^[0-9]+', '', string2)
    # numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # for word in string1:
    #     if word in numbers:
    #         str1[word] += ''
    #     else:
    #         str1[word] += string1[word]
    # print(str1)
    stop = load_stopwords("stopwords.txt")
    for index in str1:
        if index in stop:
            str1.remove(index)
    for index in str2:
        if index in stop:
            str2.remove(index)
    # print(str1)
    # print(str2)

    freq1 = {}
    freq1 = collections.Counter(str1)
    freq2 = {}
    freq2 = collections.Counter(str2)
    # print(freq1)
    # print(freq2)

    denominator1 = 0
    denominator2 = 0
    numerator = sum(freq1[word]*freq2[word] for word in freq1)
    for word in freq1:
        denominator1 += freq1[word] ** 2
    for word in freq2:
        denominator2 += freq2[word] ** 2
    # for words in freq1.keys():
    #     if freq1.keys() == freq2.keys():
    #         return wr
    denominator = math.sqrt(denominator1) * math.sqrt(denominator2)
    # # numerator = sum(freq1*freq2)
    # # denominator = sqrt(sum(freq1*freq2)) * sqrt(sum(freq1*freq2))
    return numerator/denominator
    # return numerator




def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
