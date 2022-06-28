import sys

while True:
    # 주어지는 자연수 N
    N = int(sys.stdin.readline())
    # N값이 0이라면 break
    if N == 0:
        break
    # 소수의 개수를 셀 변수 cnt
    cnt = 0
    # N보다 크고 2*N보다 작거나 같은 소수를 확인하기 위한 for문
    for i in range(N + 1, 2 * N + 1):
        # N이 자연수이기 때문에 i가 1인 경우는 고려하지 않았다.
        # 범위안에 2가 있다면 소수이므로 cnt 1 증가
        if i == 2:
            cnt += 1
            continue
        # 이 외의 i는 소수를 확인한다.
        else:
            # 2부터 i의 제곱근까지 값을 확인하고 나누어지면 소수가 아니므로 break
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    break
            # 제곱근까지 약수가 없다면 소수이므로 cnt 1 증가
            else:
                cnt += 1
    # N의 범위내 소수를 출력
    print(cnt)