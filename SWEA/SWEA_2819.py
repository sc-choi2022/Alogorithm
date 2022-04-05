def dfs(n, si, sj, num):
    # 7번 움직인 경우
    if n == 7:
        # 완성된 num값을 sset에 추가 후 return
        sset.add(num)
        return

    # 4방향에 대한 for문
    for di, dj in ((0, 1), (1, 0), (0,-1), (-1,0)):
        # 이동 후 값 ni, nj를 구하고
        ni = si + di
        nj = sj + dj
        # ni, nj가 범위에 있다면 다음 dfs를 진행
        if 0<= ni <4 and 0<= nj < 4:
            # 횟수, i, j, 이전 값*10 + 다음 값
            dfs(n+1, ni, nj, num*10 + arr[ni][nj])

# 테스트케이스 번호
T = int(input())
for case in range(1, T+1):
    # 4X4격자의 정보를 담을 리스트 arr
    arr = [list(map(int,input().split())) for _ in range(4)]
    # 만들어지는 7자리 수를 담을 set sset
    sset = set()
    # 모든 위치에서 dfs시작
    for i in range(4):
        for j in range(4):
            dfs(0, i, j, 0)
    # 테스트케이스 번호와 sset의 길이 출력
    print(f'#{case} {len(sset)}')