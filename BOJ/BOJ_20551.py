import sys

# 원소의 개수 N, 질무의 개수 M
N, M = map(int, sys.stdin.readline().split())
A = sorted([int(sys.stdin.readline()) for _ in range(N)])

for _ in range(M):
    # 정수 D
    D = int(sys.stdin.readline())

    start, end = 0, N-1
    while start <= end:
        mid = (start+end)//2

        if A[mid] < D:
            start = mid + 1
        elif A[mid] > D:
            end = mid - 1
        else:
            if end == mid:
                break
            end = mid

    # D가 B에서 처음으로 등장한 위치를 출력
    # 존재하지 않는다면 -1 출력
    print(mid if A[mid] == D else -1)