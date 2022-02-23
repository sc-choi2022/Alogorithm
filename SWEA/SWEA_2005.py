import sys
sys.stdin = open('input.txt')
# 테스트 케이스의 개수 T
T = int(input())
# 테스트 케이스 수만큼 진행하기 위한 for문
for case in range(1, T + 1):
    # 삼각형의 크기 N
    N = int(input())
    # N을 기준으로 N*N 리스트에 규칙에 맞도록 담아줄 arr
    # 지정해 줄 규칙외에 값은 1로 채운다.
    arr = [[1]*e for e in range(1, N+1)]
    # 규칙에 맞게 arr에 값을 할당
    for i in range(N):
        for j in range(N+1):
            if j >= 1 and j < i:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

	# 테스트 케이스의 번호
    print(f'#{case}')
    # arr의 각 행의 ar의 값을 출력
    for ar in arr:
        print(*ar)