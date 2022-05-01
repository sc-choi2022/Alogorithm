import sys
sys.stdin = open('sample_input.txt')

# 테스트 케이스 수 T
T = int(input())
for case in range(1, T+1):
    # 0보다 크고 1미만인 십진수 N
    N = float(input())
    # 똑같은 소수점이 나올 때까지 진행하기 위한 첫 소수점
    first = N * 2 - int(N*2)
    # 첫번째 이진수 변형의 정수부를 ans에 저장한다.
    ans = str(int(N*2))
    # N의 값을 갱신해준다.
    N = N * 2 - int(N*2)
    # 조건에 따라 break로 탈출하는 방법을 사용
    while True:
        # 13자리 이상이 필요한 경우에는 ‘overflow’를 출력 후 break
        if len(ans) >= 13:
            print(f'#{case} overflow')
            break
        # 이진수로 변형하기 위해 변수 binary에 N*2값을 할당
        binary = N*2
        # binary가 1이되거나 똑가은 소수점이 나오는 경우
        if binary == 1 or binary - int(binary) == first:
            # ans에 값을 추가하고 break
            ans += str(int(binary))
            print(f'#{case} {ans}')
            break
        # 위 조건에 걸리지 않았다면 ans에 정수부 값을 계속 추가 후 N값을 갱신한다.
        else:
            ans += str(int(N*2))
            N = N * 2 - int(N*2)