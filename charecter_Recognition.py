import math

# No of lines, no of curves, horizontal lines, vertical lines
train = [[3, 0, 1, 0], [1, 2, 0, 1], [0, 1, 0, 0], [1, 1, 0, 1], [4, 0, 3, 1],
         [3, 0, 2, 1], [2, 1, 1, 1], [3, 0, 1, 2], [1, 0, 0, 1], [2, 1, 1, 1]]
t = int(input())
result = []


# min euclidean distance calculation
def check(test):
    value = 100
    ch = -1
    for i in range(10):
        sum = 0
        for j in range(4):
            sum += math.pow(abs(test[j] - train[i][j]), 2)
        sum = math.sqrt(sum)
        if sum < value:
            value = sum
            ch = i
    return ch


# input
for i in range(t):
    test = input().split()
    for j in range(4):
        test[j] = int(test[j])
    result.append(check(test))

for i in result:
    print(chr(i + 65))
