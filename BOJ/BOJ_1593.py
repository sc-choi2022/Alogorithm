import sys

# 단어 W의 길이 g, 문자열 S의 길이 L
g, L = map(int, sys.stdin.readline().split())
# 단어 W
W = sys.stdin.readline().rstrip()
# 문자열 S
S = sys.stdin.readline().rstrip()
# S의 부분 문자열의 범위 start, end
start, end = 0, g-1

# 단어 W와 문자열 S[start:end+1]의 알파벳 개수를 저장하는 배열 Wn, Sn
Wn, Sn = [0] * 58, [0] * 58

for i in range(g):
    Wn[ord(W[i])-65] += 1
    Sn[ord(S[i])-65] += 1

# W의 순열이 S 안에 있을 수 있는 형태의 개수 answer
answer = int(Wn == Sn)

for _ in range(L-g):
    Sn[ord(S[start])-65] -= 1
    start += 1
    end += 1
    Sn[ord(S[end])-65] += 1

    if Sn == Wn:
        answer += 1

# answer 출력
print(answer)