import sys

def change(target):
    print(S, target)
    if len(S) == len(target):
        if S == target:
            return 1
        return 0
    if target[-1] == 'A':
        change(target[:-1])
    if target[0] == 'B':
        

S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()

print(change(T))