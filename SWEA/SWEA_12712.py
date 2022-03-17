import sys
sys.stdin = open('in1.txt')

T = int(input())
for case in range(1, T+1):
    # NxN 배열의 길이 N 와 파리의 스프레이 길이 M
    N, M = map(int, input().split())
    # 파리의 위치를 담은 리스트 fly
    fly = [list(map(int, input().split())) for _ in range(N)]

    # + 스프레이의 방향을 담은 리스트 di, dj
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # x 스프레이의 방향을 담은 리스트 dii, djj
    dii = [1, -1, -1, 1]
    djj = [1, 1, -1, -1]

    # 최대 파리수 초기화
    maxKill = 0
    # + 스프레이의 모든 경우에 수에서 최대 파리수를 구하는 for문
    for i in range(N):
        for j in range(N):
            tmp_sum = fly[i][j]
            for d in range(4):
                for k in range(1, M):
                    ni = i + di[d]*k
                    nj = j + dj[d]*k
                    if 0<= ni < N and 0<= nj < N:
                        tmp_sum += fly[ni][nj]
            if tmp_sum > maxKill:
                maxKill = tmp_sum
    # x 스프레이의 모든 경우에 수에서 최대 파리수를 구하는 for문
    for ii in range(N):
        for jj in range(N):
            tmp_sum1 = fly[ii][jj]
            for d in range(4):
                for kk in range(1, M):
                    nii = ii + dii[d] * kk
                    njj = jj + djj[d] * kk
                    if 0 <= nii < N and 0 <= njj < N:
                        tmp_sum1 += fly[nii][njj]

            if tmp_sum1 > maxKill:
                maxKill = tmp_sum1
    # 테스트케이스 번호와 최대 파리수 출력
    print(f'#{case} {maxKill}')