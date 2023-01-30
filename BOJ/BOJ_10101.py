import sys

# 삼각형 각의 크기를 담을 angles
angles = [int(sys.stdin.readline()) for _ in range(3)]
angles.sort()

# 세 각의 크기가 모두 60
if angles == [60, 60, 60]:
    print('Equilateral')
# 세 각의 합이 180이 아닌 경우
elif sum(angles) != 180:
    print('Error')
# 세 각의 합이 180
else:
    # 두 각이 같은 경우
    if angles[0] == angles[1] or angles[1] == angles[2]:
        print('Isosceles')
    # 같은 각이 없는 경우
    else:
        print('Scalene')