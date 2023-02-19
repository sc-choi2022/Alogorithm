import sys

# 정사각형 여부를 정할 함수 square
def square(coordinate):
    # 두 변의 각 길이의 제곱 side1, side2
    side1 = (coordinate[1][0] - coordinate[0][0])**2 + (coordinate[1][1] - coordinate[0][1])**2
    side2 = (coordinate[3][0] - coordinate[1][0])**2 + (coordinate[3][1] - coordinate[1][1])**2
    # side1과 side2의 값이 다른 경우 0 return
    if side1 != side2:
        return 0
    # side1, side2가 아닌 한 변의 길이의 제곱 side3
    side3 = (coordinate[3][0] - coordinate[2][0])**2 + (coordinate[3][1] - coordinate[2][1])**2
    # side3가 이전 두변의 길이의 제곱과 다른 경우 0 return
    if side2 != side3:
        return 0
    # 마지막 변 길이의 제곱 side4
    side4 = (coordinate[2][0] - coordinate[0][0])**2 + (coordinate[2][1] - coordinate[0][1])**2
    # side4의 길이가 나머지 세 변의 제곱 길이와 다른 경우 0 return
    if side3 != side4:
        return 0

    # 대각선의 길이의 제곱 diagonal1, diagonal2
    diagonal1 = (coordinate[3][0] - coordinate[0][0])**2 + (coordinate[3][1] - coordinate[0][1])**2
    diagonal2 = (coordinate[2][0] - coordinate[1][0])**2 + (coordinate[2][1] - coordinate[1][1])**2

    # 마름모인 경우
    if diagonal1 != diagonal2 or side1 + side2 != diagonal1:
        return 0
    return 1


# 테스트케이스 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    coordinates = [tuple(map(int, sys.stdin.readline().split())) for _ in range(4)]
    coordinates.sort(key=lambda x : (x[0], x[1]))
    # 정사각형을 만들 수 있으면 1을, 없으면 0을 출력
    print(square(coordinates))