import sys

while True:
    try:
        # 문자열 S, T
        S, T = sys.stdin.readline().rstrip().split()
        S = list(S)

        for t in T:
            if S and t == S[0]:
                S.pop(0)

        if not S:
            print('Yes')
        else:
            print('No')
    except:
        break