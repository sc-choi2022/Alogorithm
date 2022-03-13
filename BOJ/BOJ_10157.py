from pprint import pprint
# 가로 C, 세로 R
C, R = map(int, input().split())
# 대기 순서 K
K = int(input())
# 공연장의 좌석 리트스 arr
arr = [[0]*C for _ in range(R)]
# 방향에 대한 정보 di, dj
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

# 시작 번호
num = 1
# 시작하는 자리
i = -1
j = 0
d = 0
# 대기자가 좌석수 보다 많다면
if C * R < K:
    print(0)
# 그렇지 않다면
else:
    # 대기자 수만큼 좌석 배정
    while num <= K:
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni< R and 0<= nj < C and arr[ni][nj] == 0:
            i = ni
            j = nj
            arr[i][j] = num
            num += 1
        else:
            d = (d + 1)% 4
    # 0,0부터 시작했기때문에 1씩 더해준다.
    print(j+1, i+1)