import sys

# 식탁의 길이 N, 햄버거를 선택할 수 있는 거리 K
N, K = map(int, sys.stdin.readline().split())
# 문자열 words
words = list(sys.stdin.readline().rstrip())

# 햄버거를 먹을 수 있는 최대 사람의 수 answer
answer = 0
for idx in range(N):
    # idx위치가 사람의 위치인 경우
    if words[idx] == 'P':
        # 인접한 햄버거가 있는 지 확인
        for i in range(max(idx-K, 0), min(idx+K+1, N)):
            if words[i] == 'H':
                words[i] = 0
                answer += 1
                break
# answer 출력
print(answer)