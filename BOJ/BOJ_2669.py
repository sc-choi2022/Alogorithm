# x좌표와 y좌표는 1이상이고 100이하인 정수 x, y의 값을 작성할 수 있는 0으로 채운 리스트
arr = [[0]*100 for _ in range(100)]
# 면적을 더해줄 sum 초기화
sum = 0
# 네개의 직사각형에 대한 정보로 arr를 채운다.
for _ in range(4):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1
# arr의 모든 행과 열에서
for ii in range(100):
    for jj in range(100):
        # 값이 1이라면 면적값 1 증가
        if arr[ii][jj] == 1:
            sum += 1
# 네개의 직사각형이 차지하는 면적을 출력
print(sum)