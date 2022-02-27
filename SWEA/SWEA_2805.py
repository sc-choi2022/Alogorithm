import sys
sys.stdin = open('input.txt')
# 테스트 케이스의 개수 T
T = int(input())

for case in range(1, T+1):
    # NxN 행렬 N
    N = int(input())
    # NxN 행렬을 담은 arr
    arr = [list(map(int, input())) for _ in range(N)]
    ans = 0

    middle = N//2
    start = middle
    end = middle

    for i in range(len(arr)):
        for j in range(start, end+1):
            ans += arr[i][j]
        if i < middle:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1

    print(f'#{case} {ans}')