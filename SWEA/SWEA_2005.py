# 테스트 케이스의 개수 T
T = int(input())
# 테스트 케이스 수만큼 진행하기 위한 for문
for case in range(1, T + 1):
    # 삼각형의 크기 N
    N = int(input())
    # N을 기준으로 N*N 리스트에 규칙에 맞도록 담아줄 arr
    arr = [[0]*N for _ in range(N)]
    # 규칙에 맞게 arr에 값을 할당
    for i in range(N):
        for j in range(i+1):
            if i == 0 and i==j:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
	# 테스트 케이스의 번호
    print(f'#{case}')
    # arr 안에 값이 0이 아니라면 출력
    for ar in arr:
        for a in ar:
            if a != 0:
                # 행 단위로 출력하기 위한 print()
                print(a, end=' ')
        print()