import sys

# 딱지놀이의라운드 수 자연수 N
N = int(sys.stdin.readline())

for _ in range(N):
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    lenA, lenB = A.pop(0), B.pop(0)

    for i in range(4, 0, -1):
        if A.count(i) > B.count(i):
            print("A")
            break
        elif A.count(i) < B.count(i):
            print("B")
            break
    else:
        print("D")