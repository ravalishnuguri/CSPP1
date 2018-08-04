'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str1 = str(input())
    str2 = ""
    length = len(str1)
    i = 0
    while i < length:
        if str1[i] in ('!', '@', '#', '$', '%', '^', '&', '*'):
            str2 += " "
        else:
            str2 += str1[i]
        i = i+1
    print(str2)
if __name__ == "__main__":
    main()
