'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math

# def similarity(dict1, dict2):
#     '''
#         Compute the document distance as given in the PDF
#     '''
#     dict1 = dict1.lower()
#     dict2 = dict2.lower()

#     # str1 = re.sub(r'[^a-z]', '', dict1).split()
#     # str2 = re.sub(r'[^a-z]', '', dict2).split()
#     str1 = re.findall(r"[a-zA-Z]+", dict1, re.MULTILINE)
#     str2 = re.findall(r"[a-zA-Z]+", dict2, re.MULTILINE)
#     # str1 = re.sub(r'^[0-9]+', '', string1)
#     # str2 = re.sub(r'^[0-9]+', '', string2)
#     # numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     # for word in string1:
#     #     if word in numbers:
#     #         str1[word] += ''
#     #     else:
#     #         str1[word] += string1[word]
#     # print(str1)
#     stop = load_stopwords("stopwords.txt")
#     for index in str1:
#         if index in stop:
#             str1.remove(index)
#     for index in str2:
#         if index in stop:
#             str2.remove(index)
#     # print(str1)
#     # print(str2)

#     freq1 = {}
#     freq1 = collections.Counter(str1)
#     freq2 = {}
#     freq2 = collections.Counter(str2)
#     # print(freq2)

#     denominator1 = 0
#     denominator2 = 0
#     numerator = sum(freq1[word]*freq2[word] for word in freq1)
#     for word in freq1:
#         denominator1 += freq1[word] ** 2
#     for word in freq2:
#         denominator2 += freq2[word] ** 2
#     # for words in freq1.keys():
#     #     if freq1.keys() == freq2.keys():
#     #         return wr
#     denominator = math.sqrt(denominator1) * math.sqrt(denominator2)
#     # # numerator = sum(freq1*freq2)
#     # # denominator = sqrt(sum(freq1*freq2)) * sqrt(sum(freq1*freq2))
#     return numerator/denominator
#     # return numerator
def calculation(dictionary):
    '''calculation for the program'''
    num = 0
    denom1 = 0
    denom2 = 0
    for index in dictionary:
        num += dictionary[index][0] * dictionary[index][1]
    for index in dictionary:
        denom1 += dictionary[index][0] ** 2
    for index in dictionary:
        denom2 += dictionary[index][1] ** 2
    return num/(math.sqrt(denom1) * math.sqrt(denom2))

def tokens(data):
    '''converting text file into list'''
    data = data.lower()
    data = re.sub('[^a-z\ ]', '', data)
    swords = load_stopwords("stopwords.txt")
    data = data.strip().split(" ")
    list1 = []
    for word in data:
        # k = re.sub(r'[^a-z\1]','',word).strip()
        if word not in swords and len(word) > 0:
            list1.append(word)
    return list1
def freq(dictionary, data, index):
    '''finding out the frequency of the data'''
    for index in data:
        if data not in dictionary:
            dictionary[data] = [0, 0]
            dictionary[data][index] += 1
        else:
            dictionary[data][index] += 1
    return dictionary
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    dictionary = {}
    dict1 = tokens(dict1)
    dict2 = tokens(dict2)
    dictionary = freq(dictionary, dict1, 0)
    dictionary = freq(dictionary, dict2, 1)
    result = calculation(dictionary)
    return result



def load_stopwords(_):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(_, 'r') as _:
        for line in _:
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
