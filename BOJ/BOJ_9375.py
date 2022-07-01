import sys
# 테스트케이스 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 의상의 수 N
    N = int(sys.stdin.readline())
    # 의상의 종류를 나누어 담을 딕셔너리 custum
    custum = dict()

    # N개의 의상을 확인하여
    for i in range(N):
        # 의상 이름과 의상의 종류를 나누어 받고 custum에 의상 종류에 맞춰 의상 이름을 저장한다.
        item, part = sys.stdin.readline().split()
        if part not in custum:
            custum[part] = [item]
        else:
            custum[part] = custum[part] + [item]
    # 출력할 결과 ans를 1로 초기화
    ans = 1
    # key의 value에 입지 않은 경우도 있기 때문에 1을 더한 값을 모든 custum의 item에 곱해준다.
    for key in custum:
        ans *= len(custum[key]) + 1
    # 알몸은 제외해야하므로 ans - 1를 출력
    print(ans - 1)