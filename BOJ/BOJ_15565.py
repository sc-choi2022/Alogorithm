import sys

# 전체 인형의 개수 N, 라이언 인형의 연속 개수 기준 K
N, K = map(int, sys.stdin.readline().split())
# 인형의 정보를 저장하는 배열 dolls
dolls = list(map(int, sys.stdin.readline().split()))
# 인형들의 집합의 크기 기준 left, right
left, right = 0, 0
# 구간의 라이언 인형의 개수
cnt = 0 if dolls[0] == 2 else 1
answer = 1e6 + 1

while right < N:
    # 라이언 인형 개수가 K인 경우
    if cnt == K:
        answer = min(answer, right - left + 1)
        if dolls[left] == 1:
            cnt -= 1
        left += 1
    # 라이언 인형 개수가 K가 아닌 경우
    else:
        right += 1
        if right < N and dolls[right] == 1:
            cnt += 1
# K개 이상의 라이언 인형을 포함하는 가장 작은 연속된 인형들의 집합의 크기를 출력
# 그런 집합이 없다면 -1을 출력
print(-1 if answer == 1e6+1 else answer)