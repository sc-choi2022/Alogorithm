import sys

# 테스트 케이스 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 통나무의 개수 N
    N = int(sys.stdin.readline())
    # 통나무의 높이를 담은 배열 L
    L = sorted(list(map(int, sys.stdin.readline().split())))
    answer = 0
    for i in range(2, N):
        answer = max(answer, abs(L[i]-L[i-2]))
    # 통나무들로 만들 수 있는 최소 난이도 출력
    print(answer)