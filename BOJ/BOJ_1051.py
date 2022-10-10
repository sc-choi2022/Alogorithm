import sys
# 직사각형의 세로길이 N, 가로길이 M
N, M = map(int, sys.stdin.readline().split())
# 직사각형의 정보를 담은 square와 transpose 정보를 담은 배열 trans
square = [list(sys.stdin.readline().strip()) for _ in range(N)]
trans = list(zip(*square))
# 정사각형의 한 변의 길이 cnt
cnt = 0

for i in range(N):
    for j in range(M):
        # 현재 위치 (i, j)의 값을 변수 value에 저장
        value = square[i][j]
        # 사각형을 만들수 있는 위치임을 확인
        if square[i].count(value) > 1 and trans[j].count(value) > 1:
            # 가능한 정사각형 변의 길이를 변수 able에 저장
            able = min(N-i, M-j)
            for k in range(cnt, able):
                # 정사각형 꼭짓점의 값이 모두 동일하다면 cnt값을 갱신
                if value == square[i+k][j] and value == square[i][j+k] and value == square[i+k][j+k]:
                    cnt = k
# 정사각형의 크기를 출력
print((cnt + 1)**2)