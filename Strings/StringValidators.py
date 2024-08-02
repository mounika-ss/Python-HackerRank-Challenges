if __name__ == '__main__':
    s = input()
    
# Python provides built-in string validation methods for basic data in strings
# Task is to find out if the string S contains any of :
# alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
# that is to find each character in the string, direclty not for whole string as like s.isalnum()
    
# here iam using 'any()' function, to check if any element in an iterable is True.
print(any(i.isalnum() for i in s))
print(any(i.isalpha() for i in s))
print(any(i.isdigit() for i in s))
print(any(i.islower() for i in s))
print(any(i.isupper() for i in s))
