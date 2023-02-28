import sys

def location(num, n):
    # 첫번째 학생인 경우
    if len(sit) == 0:
        seat[1][1] = num
        sit[num] = (1, 1)
        return
    # 조건을 만족하는 칸을 담을 배열 able
    able = []
    # 1번 조건인 좋아하는 학생 수의 최대 명수 cnt
    cnt = 0

    for i in range(N):
        for j in range(N):
            # (i, j)의 인접의 좋아하는 학생 수 tmp, 빈칸의 수 blank
            tmp, blank = 0, 0
            if seat[i][j] == 0:
                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                    ni, nj = i + di, j + dj
                    # 인접한 칸이 가능한 칸인 경우
                    if 0 <= ni < N and 0 <= nj < N:
                        # 좋아하는 학생인 경우 tmp 1 증가
                        if seat[ni][nj] in friends[n]:
                            tmp += 1
                        # 빈칸인 경우 blank 1 증가
                        elif seat[ni][nj] == 0:
                            blank += 1
                # cnt와 tmp가 동일한 경우 (i, j, blank)를 able에 추가
                if tmp == cnt:
                    able.append((i, j, blank))
                # tmp가 cnt보다 큰 경우 cnt와 able을 갱신
                elif tmp > cnt:
                    cnt = tmp
                    able = [(i, j, blank)]
    # 조건 2와 3에 따라 able을 정렬
    able.sort(key=lambda x: (-x[2], x[0], x[1]))
    # 가장 조건에 부합하는 0번 인덱스 값을 변수 r, c, b에 저장
    r, c, b = able[0]
    # seat[r][c]에 num을 배치
    seat[r][c] = num
    # num의 위치값을 딕셔너리 sit에 저장
    sit[num] = (r, c)

# 교실의 크기 NxN
N = int(sys.stdin.readline())
# 학생의 번호와 좋아하는 학생의 번호를 저장하는 배열 friends
friends = [0] * (N ** 2)
# 자리배치를 저장할 배열 seat
seat = [[0] * N for _ in range(N)]
# 이미 앉은 학생의 번호을 저장할 딕셔너리 sit
sit = {}

# 만족도 satisfaction
satisfaction = 0
# 만족도 기준과 만족도를 담은 리스트 criteria
criteria = {0 : 0, 1: 1, 2: 10, 3: 100, 4: 1000}

for n in range(N**2):
    # 정보를 담을 배열 friends
    friends[n] = list(map(int, sys.stdin.readline().split()))
    # 학생번호 num
    num = friends[n][0]
    # 함수 location으로 num의 자리배치
    location(num, n)

for friend in friends:
    # friend의 첫 값인 학생의 번호를 변수 student에 저장
    student = friend[0]
    # sit에 저장된 student의 위치를 변수 ci, cj에 저장
    ci, cj = sit[student]
    # student의 인접한 칸의 좋아하는 학생의 수 like
    like = 0
    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = ci + di, cj + dj
        # 인접한 칸의 좋아하는 학생수를 확인 후 like 1 증가
        if 0 <= ni < N and 0 <= nj < N and seat[ni][nj] in friend:
            like += 1
    # 딕셔너리 criteria[like]값을 satisfaction에 더한다.
    satisfaction += criteria[like]
# 학생의 만족도의 총 합을 출력
print(satisfaction)