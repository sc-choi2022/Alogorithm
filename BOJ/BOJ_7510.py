import sys

# 테스트케이스의 개수 n
n = int(sys.stdin.readline())

for i in range(1, n+1):
    length = sorted(list(map(int, sys.stdin.readline().split())))
    print(f'Scenario #{i}:')
    if length[2]**2 == (length[0]**2 + length[1]**2):
        print('yes')
    else:
        print('no')
    print()