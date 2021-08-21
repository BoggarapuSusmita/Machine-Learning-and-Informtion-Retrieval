import math

import pandas as pd

# No of lines, no of curves, horizontal lines, vertical lines
df = pd.read_csv("char.csv")
train = [list(row) for row in df.values]
t = int(input("Enter Test Cases : "))
result1, result2 = [], []


# min euclidean distance calculation
def calc_dist(i, j):
    sum = 0
    for k, l in zip(i, j):
        sum += math.pow(abs(k - l), 2)
    sum = math.sqrt(sum)
    return sum


def check1(test):
    val = 100
    for i in range(10):
        res = calc_dist(train[i], test)
        if res < val:
            val = res
            ch = i
    return ch


# POSTPROCESSING - Points of intersection
df1 = pd.read_csv("char2.csv")
train1 = [list(row) for row in df1.values]


def check2(test):
    val = 100.0
    ch = 0
    for i in range(10):
        p = train[i] + train1[i]
        res = calc_dist(p, test)
        if res < val:
            val = res
            ch = i
    return ch


for i in range(t):
    test = input().split()
    for j in range(5):
        test[j] = int(test[j])
    result1.append(check1(test[:4]))
    result2.append(check2(test[:5]))

for i,j in zip(result1,result2):
    print("Before Post Processing : ",chr(i + 65))
    print("After Post Processing : ",chr(j + 65))
    print()
