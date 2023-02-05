import sys

# 테스트 케이스 개수 T
T = int(sys.stdin.readline())

# 제곱에 관련된 정보를 담은 info
info = {2: [2, 4, 8, 6], 3: [3, 9, 7, 1], 4: [4, 6], 7: [7, 9, 3, 1], 8: [8, 4, 2, 6], 9: [9, 1]}

for _ in range(T):
    # 밑 A와 지수 B
    A, B = map(int, sys.stdin.readline().split())
    # 밑은 1의 자리가 결과의 마지막 자리숫자를 결정하므로 변수 a에 10으로 나눈 나머지를 저장
    a = A % 10
    # a와 동일한 번호의 컴퓨터가 마지막인 경우
    if a in (1, 5, 6):
        print(a)
    # a가 0인 경우
    elif a == 0:
        print(10)
    # a를 key로 info의 가능한 배열에서 컴퓨터 번호를 확인할 필요가 있는 경우
    else:
        b = info[a]
        print(b[B%(len(b)) - 1])