# 테스트케이스 T
T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    # 이동거리 dist
    dist = y-x
    n = 0
    while True:
        # 이동 횟수의 경계값 확인
        if dist <= n*(n+1):
            break
        n += 1
    # 공간이동 작동 횟수가 홀수인 경우
    if dist <= n**2:
        print(n*2-1)
    # 공간이동 작동 횟수가 짝수인 경우
    else:
        print(n*2)