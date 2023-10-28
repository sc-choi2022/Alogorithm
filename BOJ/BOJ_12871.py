import sys

S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()

lenS, lenT = len(S), len(T)

if T*lenS == S*lenT:
    print(1)
else:
    print(0)