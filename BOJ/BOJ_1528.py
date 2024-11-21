from collections import deque
import sys

# 금민수의 합으로 나타내야하는 정수 N
N = int(sys.stdin.readline())
gold = []

for i in range(2, 200):
    bi = []
    s = ''
    tmp = i
    while tmp:
        bi.append(tmp%2)
        tmp //= 2
    for j in range(len(bi)-1, -1, -1):
        if j == len(bi)-1:
            continue
        if bi[j] == 0:
            s += '4'
        else:
            s += '7'
    gold.append(int(s))
print(gold)