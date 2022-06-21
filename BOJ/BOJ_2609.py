import sys
# 주어지는 자연수 N1, N2
N1, N2 = map(int, sys.stdin.readline().split())

if N1 == N2:
    print(N1)
    print(N2)
else:
    # N1과 N2 중 작은 수를 less, 큰수를 more 변수에 할당한다.
    less = min(N1, N2)
    more = max(N1, N2)

    # 약수를 구하기 위한 변수 check
    check = 1
    # 최대공약수 GCD
    GCD = 1
    # 최대 공약수가 less가 될 수 있으므로 less와 같을 때까지 while문을 실행
    while less >= check:
        # check가 공약수가 아니라면 check 1 증가 후 continue
        if less % check or more % check:
            check += 1
            continue
        # check가 공약수가 맞다면 GCD에 할당 후 1 증가
        GCD = check
        check += 1
    # 최대 공약수와 최대공약수를 활용하여 계산한 최소공배수 출력
    print(GCD)
    print(GCD * (N1 // GCD) * (N2 // GCD))