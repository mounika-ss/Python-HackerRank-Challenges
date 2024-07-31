def mutate_string(string, position, character):
    # to replace the position of string with character
    
    # approach, convert string to list(string), then change value and join
    # another approach, to slice the string and join it back
     
    string = string[:position] + character + string[position+1:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
