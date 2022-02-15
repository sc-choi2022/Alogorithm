import sys
sys.stdin = open("input.txt")

# 10번의 케이스에 대해
for _ in range(1, 10 + 1):
    # 테스트 케이스의 번호 받기
    case = int(input())
    # 100 x 100 크기의 2차원 배열을 arr에 할당
    arr = [list(map(int, input().split())) for _ in range(100)]
    min_ans = 10000 #모든 칸을 지났을 경우
    ans = -1

    # 100개의 열 중에 1인 값만을 찾는 for문
    for k in range(100):
        if arr[0][k] != 1:
            continue

        # 가는 거리를 세는 cnt 초기화
        cnt = 0
        # 0번째 행부터 k번째 열까지
        i, j = 0, k
        j = k
        # 좌측에서 우측가는 방향, 우측에서 좌측으로 가는 방향 확인을 위해
        # l_r 와 r_l를 True로 설정
        l_r = True
        r_l = True
        while True:
            # 마지막 행에 도착하면 거리를 비교하는 for문
            if i == 99:
                if min_ans > cnt:
                    min_ans = cnt
                    ans = k
                break
            # 행이 범위를 벗어나지 않음, 오른쪽 칸에 1이 있음, 좌측에서 우측으로 가는 방향가능 확인 조건
            if j != 99 and arr[i][j + 1] == 1 and l_r == True:
                # 우측에서 좌측으로 가는 방향을 멈춤
                r_l = False
                # 오른쪽 열로 이동
                j += 1
            # 행이 번위를 벗어나지 않음, 왼쪽 칸에 1이 있음, 우측에서 좌측로 가는 방향가능 확인 조건
            elif j != 0 and arr[i][j - 1] == 1 and r_l == True:
                # 좌측에서 우측으로 가는 방향을 멈춤
                l_r = False
                # 왼쪽 열로 이동
                j -= 1
            elif arr[i + 1][j] == 1:
                # 방향 이동하는 확인 조건 초기화
                r_l = True
                l_r = True
                # 다음 행으로 이동
                i += 1
            # 한번 움직일 때마다 1씩 증가
            cnt += 1
    # 케이스의 번호 출발점의 x좌표 출력
    print(f'#{case} {ans}')