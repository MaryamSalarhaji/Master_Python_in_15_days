#Create a Python function to check if a given string is a palindrome.
string = input ("Enter a string:")
def reversed_string (string):
    rever_string = string[:: -1]
    if rever_string == string:
        return "The string is palindrome"
    else:
        return "The string is not palindrome"


print(reversed_string(string))
