def count_substring(string, sub_string):
    #  to print the number of times that the substring occurs in the given string

    occurrences = 0
    for i in range(len(string)):
        if (string[i: i+len(sub_string)] == sub_string):
            occurrences += 1
    return occurrences

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
