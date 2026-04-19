import sys

# 테스트 케이스 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 부피 N
    N = int(sys.stdin.readline())

    # 부피 N인 예쁜 케이크를 만들 수 있는 경우
    if N%9 == 0 or N%3 == 2:
        print('TAK')
    # 만들 수 없는 경우
    else:
        print('NIE')