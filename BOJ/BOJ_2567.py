import sys

# 색종이의 수 N
N = int(sys.stdin.readline())
# 색종이를 붙이는 도화지 paper
paper = [[0]*101 for _ in range(101)]

for _ in range(N):
    # 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리 A
    # 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리 B
    A, B = map(int, sys.stdin.readline().split())

    for pi in range(A, A+10):
        for pj in range(B, B+10):
            paper[pi][pj] = 1
answer = 0
for i in range(101):
    for j in range(101):
        if paper[i][j]:
            # 위치주변의 색종이 개수 tmp
            tmp = 0
            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                if paper[i+di][j+dj]:
                    tmp += 1
            # 변인 경우
            if tmp == 3:
                answer += 1
            # 모서리인 경우
            elif tmp == 2:
                answer += 2

# 색종이가 붙은 검은 영역의 둘레의 길이를 출력
print(answer)