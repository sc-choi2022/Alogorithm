import sys
sys.stdin = open('sample_input.txt')

# 테스트 케이스의 수 T
T = int(input())
for case in range(1,T+1):
    # 길이가 1이상 15이하인 문자열을 담을 5X15의 리스트를 문자열에 포함되지 않는 '.'로 채움
    arr = [['.']*15 for _ in range(5)]
    # 출력할 답 ans를 초기화
    ans = ''

    # 각 행에 대해
    for i in range(5):
        # 다섯 줄의 문자열을 받아 arr에 길이에 맞춰 넣어준다.
        string = list(input())
        for j in range(len(string)):
            arr[i][j] = string[j]

    # arr의 값 중 초기화 값 '.'이 아닌 값을 출력 ans에 이어붙인다.
    for jj in range(15):
        for ii in range(5):
            if arr[ii][jj] != '.':
                ans += arr[ii][jj]

    # 테스트 케이스마다 #T 세로로 읽은 순서대로 글자들을 출력
    print(f'#{case} {ans}')