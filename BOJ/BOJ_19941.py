import sys

# 식탁의 길이 N, 햄버거를 선택할 수 있는 거리 K
N, K = map(int, sys.stdin.readline().split())
# 문자열 words
words = list(sys.stdin.readline().rstrip())

answer = 0
for idx in range(N):
    if words[idx] == 'P':
        for i in range(max(idx-K, 0), min(idx+K+1, N)):
            if words[i] == 'H':
                words[i] = 0
                answer += 1
                break
# 햄버거를 먹을 수 있는 최대 사람 수 출력
print(answer)