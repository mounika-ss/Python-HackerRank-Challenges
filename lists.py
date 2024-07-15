if __name__ == '__main__':
    N = int(input()) # number of commands

    list_int = [] # elements list
    for _ in range(N):
        command, *items = input().split() # for command and elements or items
        items = list(map(int, items))

        if command == 'insert':
            list_int.insert(items[0], items[1])
        elif command == 'remove':
            list_int.remove(items[0])
        elif command == 'append':
            list_int.append(items[0])
        elif command == 'sort':
            list_int.sort() 
        elif command == 'pop':
            list_int.pop()
        elif command == 'print':
            print(list_int)
        elif command == 'reverse':
            list_int.reverse()
