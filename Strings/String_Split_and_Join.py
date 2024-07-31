def split_and_join(line):
    # line is a string, we have to Split the string and join using a -
    split_line = line.split(' ') 
    joined_splits = '-'.join(split_line)
    
    return joined_splits

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
