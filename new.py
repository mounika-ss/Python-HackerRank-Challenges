import math
count = 0
for i in range(3,9+1):
    if math.sqrt(i) == math.floor(i/2):
        count = count + 1
print(count)
