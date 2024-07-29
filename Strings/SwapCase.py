def swap_case(s):
    # return s.swapcase()
    # use list for join as ''.join(list of items in string)
    s_swap = ''
    for i in s:
        # if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if i.isupper():
            s_swap = s_swap + i.lower()
        elif i.islower():
            s_swap = s_swap + i.upper()
        else:
            s_swap = s_swap + i
    return s_swap

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
