import sys

def check():
    global ans
    for i in range(R):
        for j in range(C):
            if farm[i][j] == 'W':
                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                    ni, nj = i + di, j + dj

                    if 0 <= ni < R and 0 <= nj < C and farm[ni][nj] == 'S':
                        ans = True
                        break
            elif farm[i][j] == '.':
                farm[i][j] = 'D'

# 목장의 크기 R, C
R, C = map(int, sys.stdin.readline().split())
# 목장의 정보를 담을 배열 farm
farm = [list(sys.stdin.readline()) for _ in range(R)]
# 늑대가 양에게 갈 수 있는 여부를 담을 변수 ans
ans = False
# 함수 check 실행
check()

# 울타리를 어떻게 설치해도 늑대가 양이 있는 칸으로 갈 수 있는 경우
if ans:
    print(0)
# 늑대가 양이 있는 칸으로 갈 수 없게 할 수 있는 경우
else:
    print(1)
    for f in farm:
        print(''.join(f))