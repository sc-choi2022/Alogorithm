import sys

# N각형의 N
N = int(sys.stdin.readline())
# 좌표들을 담을 배열 coordinates
coordinates = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
coordinates.append(coordinates[0])
# N각형의 넓이을 외적으로 구하기 위해 더해지는 값, 빼지는 값을 area1, area2
area1, area1 = 0, 0

for i in range(N):
    areaX += coordinates[i][0] * coordinates[i+1][1]
    areaY += coordinates[i][1] * coordinates[i+1][0]
# 1/2*area를 소수점 아래 둘째 자리에서 반올림하여 첫째 자리까지 출력
print(round(abs((areaX - areaY) * 1/2), 1))