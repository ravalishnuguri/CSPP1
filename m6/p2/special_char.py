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
    str2 = "!@#$%^&*"
    count = 0
    for i in range(0,len(str1),1):
    	if(i == '!'and i=='@' and i=='#' and i=='$' and i=='%' and i=='^' and i=='&' and i=='*'):
    		count = count+1
    	if(count == 1):
    		str1[i] = " "
    		
    print(str1)

if __name__ == "__main__":
    main()
