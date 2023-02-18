import sys

# 정사각형 여부를 정할 함수 square
def square(coordinate):
    


# 테스트케이스 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    coordinates = [tuple(map(int, sys.stdin.readline().split())) for _ in range(4)]
    coordinates.sort(key=lambda x : (x[0], x[1]))
    print(square(coordinates))