import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(1, T+1):
    N = int(input())
    ans = -1
    # 세제곱근을 1/3제곱을 통해 구하고 그 값을 소숫점 두자리까지해서 value 변수에 할당
    value = round(N**(1/3),2)
    
    # value값과 value값의 정수값을 비교하여 동일하다면 ans값을 int(value)로 재할당
    if value == int(value):
        ans = int(value)
    # 테스트케이스 번호와 ans를 출력
    print(f'#{case} {ans}')