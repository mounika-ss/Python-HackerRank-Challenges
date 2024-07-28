if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
# n is the length of the arr
# here to print runner score that is not winner that is second position or second maximum score
arr = sorted(set(arr))
print(arr[-2])
