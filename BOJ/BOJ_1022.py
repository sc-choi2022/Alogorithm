import sys

# 주어지는 위치 R1, C1, R2, C2
R1, C1, R2, C2 = map(int, sys.stdin.readline().split())
# 소용돌이의 숫자를 저장하는 배열 vortex
vortex = [[0]*(C2-C1+1) for _ in range(R2-R1+1)]
# 채워지는 숫자의 개수 cnt
cnt = (C2-C1+1) * (R2-R1+1)
# 방향의 정하는 변수 D
D = 0
# 방향을 저장하는 딕셔너리 directions
directions = {0: (0, 1), 1: (-1, 0), 2: (0, -1), 3: (1, 0)}
# 소용돌이를 확인하는 숫사 number
number = 1
# 변의 길이 L
L = 1
# 소용돌이의 위치 (R, C)를 초기위치 (0, 0)로 저장
R, C = 0, 0
# 수의 길이를 확인하기 위해 마지막 수를 저장하는 변수 end
end = 0

while cnt > 0:
    # 소용돌이는 두 변마다 길이 변경된다.
    for _ in range(2):
        for _ in range(L):
            if R1 <= R <= R2 and C1 <= C <= C2:
                vortex[R-R1][C-C1] = number
                cnt -= 1
                end = number
            R, C = R + directions[D][0], C + directions[D][1]
            number += 1
        D = (D+1)%4
    L += 1
# 조정해야하는 길이 M
M = len(str(end))

for vi in vortex:
    for vj in vi:
        # 왼쪽에서부터 공백을 삽입해 길이를 맞추어 출력
        print(str(vj).rjust(M), end=' ')
    print()