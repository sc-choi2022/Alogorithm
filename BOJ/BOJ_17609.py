import sys

# 주어지는 문자열의 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    word = list(sys.stdin.readline().rstrip())
    reverse = word[::-1]
    N = len(word)
    cnt, idx = 0, 0
    for i in range(N//2 + 1):
        if word[i] != reverse[idx]:
            if word[i] == reverse[idx+1]:
                cnt += 1
                idx += 1
            elif word[i] == reverse[idx-1]:
                cnt += 1
                idx -= 1
            else:
                cnt = 2
        if cnt > 1:
            print(2)
            break
        idx += 1
    if cnt == 0:
        print(0)
    elif cnt == 1:
        print(1)