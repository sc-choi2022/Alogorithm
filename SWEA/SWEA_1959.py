import sys
sys.stdin = open('input.txt')
T = int(input())
for case in range(1, T+1):
    # 숫자열 Aj의 숫자 수 N, 숫자열 Bj의 숫자 수 M
    N, M = map(int, input().split())
    # 숫자열 Aj의 숫자를 담은 리스트 A
    A = list(map(int, input().split()))
    # 숫자열 Bj의 숫자를 담은 리스트 B
    B = list(map(int, input().split()))
    # 가장 큰 합 max_sum 값 초기화
    max_sum = 0

    # N와 M을 비교하여 길이에 따라
    # 짧은 쪽은 sm, short 긴쪽은 lg, long 변수에 할당
    if N <= M:
        sm = N
        lg = M
        short = A
        long = B
    elif N > M:
        sm = M
        lg = N
        short = B
        long = A

    # 긴 숫자열의 첫 문자를 기준으로
    for i in range(lg-sm+1):
        # 임시 합 초기화
        temp_sum = 0
        # 짧은 숫자열의 값과 곱하고 더하여 temp_sum 구함
        for j in range(sm):
            temp_sum += long[i+j]*short[j]
        # temp_sum과 max_sum 비교하여 큰 값을 max_sum에 할당
        if temp_sum > max_sum:
            max_sum = temp_sum
    # 테스트 케이스의 번호와 정답 출력
    print(f'#{case} {max_sum}')