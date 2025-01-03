import sys

# x좌표와 y좌표는 1이상이고 100이하인 정수 x, y의 값을 작성할 수 있는 0으로 채운 배열 matrix
matrix = [[0]*100 for _ in range(100)]
# 면적 answer
answer = 0

for _ in range(4):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            matrix[i][j] = 1

for ii in range(100):
    answer += sum(matrix[ii])

# 네개의 직사각형이 차지하는 면적 answer 출력
print(answer)