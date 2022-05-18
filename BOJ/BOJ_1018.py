# M×N 크기의 보드의 M, N
N, M = map(int, input().split())
# 체스판을 색칠하는 두가지 경우 p1, p2
p1 = list('WBWBWBWB')
p2 = list('BWBWBWBW')

# 8×8 크기의 체스판으로 자르는 정답 두가지 right1, right2
right1 = [p1, p2, p1, p2, p1, p2, p1, p2]
right2 = [p2, p1, p2, p1, p2, p1, p2, p1]

# N개의 줄에는 보드의 각 행의 상태를 담은 리스트 arr
arr =[list(input()) for _ in range(N)]

# 출력할 최솟값 min_count를 64로 초기화
min_count = 64
# for문을 통해 8을 기준으로 하여
for i in range(N-8+1):
    for j in range(M-8+1):
        cnt1 = 0
        cnt2 = 0
        # right1 또는 right2를 기준으로 cnt1를 세고
        for ii in range(8):
            for jj in range(8):
                if arr[i+ii][j+jj] != right1[ii][jj]:
                    cnt1 += 1

                if arr[i+ii][j+jj] != right2[ii][jj]:
                    cnt2 += 1
        # 최솟값을 갱신한다.
        if min_count > min(cnt1, cnt2):
            min_count = min(cnt1, cnt2)

# 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력
print(min_count)