#WAP TO PRINT LONGEST SUBSTRING OF GIVEN STRING WHICH DOES NOT HAVE REPEATED LETTERS
def longest_substring_length(st):
    substring=""
    list_of_substrings = []
    length_of_longest_substring = 0
    for letter in st:
        if letter not in substring:
            substring+=letter
        else:
            list_of_substrings.append(substring)
            substring=letter
            # if len(substring) > length_of_longest_substring:
            #     length_of_longest_substring = len(substring)
    
    list_of_substrings.append(substring)
    # if len(substring) > length_of_longest_substring:
    #             length_of_longest_substring = len(substring)
    for string in list_of_substrings:
        if len(string) > length_of_longest_substring:
            length_of_longest_substring = len(string)
    # print("")

    print("List of substrings which does not contain repeated letters : ",list_of_substrings)
    print("Length of longest substring :",length_of_longest_substring)
    return length_of_longest_substring

#Decorator Example :

#WAP TO PRINT FACTORIAL OF GIVEN NUMBER 
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)

def fact1(n):
    return 1 if (n==1 or n==0) else n*fact1(n-1)

#Factorial program using lambda function .
def fact2(n):
    a = lambda n : 1 if (n==0 or n==1) else n*a(n-1)
    # print(a(n),"===")
    return a(n)