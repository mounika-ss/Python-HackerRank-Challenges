if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split()) # n space-separeted integers
    
    t = tuple(integer_list)
    # print result of hash(tuple t)
    print(hash(t))
