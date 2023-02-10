import sys

# 세변의 길이
length = list(map(int, sys.stdin.readline().split()))

while True:
    if length == [0, 0, 0]:
        break
    length.sort()

    # 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우
    if length[0] + length[1] <= length[2]:
        print('Invalid')
    # 세 변의 길이가 모두 같은 경우
    elif length[0] == length[1] and length[1] == length[2]:
        print('Equilateral')
    # 세 변의 길이가 모두 다른 경우
    elif length[0] != length[1] and length[1] != length[2]:
        print('Scalene')
    # 두 변의 길이만 같은 경우
    else:
        print('Isosceles')

    length = list(map(int, sys.stdin.readline().split()))