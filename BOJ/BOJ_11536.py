import sys

# 이름의 개수 N
N = int(sys.stdin.readline())
# 선수들의 이름을 저장하는 배열 names
names = [sys.stdin.readline().rstrip() for _ in range(N)]

# 증가하는 순
if names == sorted(names):
    print('INCREASING')
# 감소하는 순
elif names == sorted(names, reverse=True):
    print('DECREASING')
# 두 경우가 아닌 경우
else:
    print('NEITHER')