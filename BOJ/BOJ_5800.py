import sys

# 반의 수 K
K = int(sys.stdin.readline())

for i in range(1, K+1):
    # 반의 번호 출력
    print(f'Class {i}')
    N, *scores = list(map(int, sys.stdin.readline().split()))
    scores.sort(reverse=True)
    gap = 0

    for j in range(1, N):
        if abs(scores[j-1]-scores[j]) > gap:
            gap = abs(scores[j-1]-scores[j])
    # 가장 높은 점수, 낮은 점수, 성적을 내림차순으로 정렬했을 때 가장 큰 인접한 점수 차이 출력
    print(f'Max {scores[0]}, Min {scores[-1]}, Largest gap {gap}')