import sys

def binary_search(a):
    start, end = 0, M-1
    result = -1

    while start <= end:
        mid = (start + end) // 2
        if B[mid] < a:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

# 테스트케이스 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # A의 수 N, B의 수 M
    N, M = map(int, sys.stdin.readline().split())
    # 각 A와 B의 크기를 저장하는 A, B
    A = sorted(list(map(int, sys.stdin.readline().split())))
    B = sorted(list(map(int, sys.stdin.readline().split())))

    # A가 B보다 큰 쌍의 개수 answer
    answer = 0

    for a in A:
        answer += binary_search(a) + 1

    # A가 B보다 큰 쌍의 개수를 출력
    print(answer)
