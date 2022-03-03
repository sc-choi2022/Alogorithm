import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(1, T+1):
    # 괄호 정보를 담은 리스트 arr
    arr = list(input())
    # 쌓이는 막대기 수
    cnt = 0
    # 잘려서 생기는 막대기 수
    ans = 0

    # 괄호 정보에 대해
    for i in range(len(arr)):
        # 값이 (이라면 쌓이는 막대기 수 cnt 1 증가
        if arr[i] == '(':
            cnt += 1
        # 값이 )이라면 두가지 경우의 수를 확인
        elif arr[i] == ')':
            # 이전 값이 (이라면 레이저
            if arr[i-1] == '(':
                # 이전 괄호가 새로운 막대기를 의미하는 것이 아니었으므로 1 감소
                cnt -= 1
                # 쌓인 막대기 수만큼 ans가 cnt 증가
                ans += cnt
            # 이전 값이 (이 아니라면 막대기의 끝
            elif arr[i-1] == ')':
                # 막대기 수가 1 감소
                cnt -= 1
                # 끝이나 막대기 1 추가
                ans += 1
    # 테스트 케이스 번호와 잘려진 조각의 총 개수 출력
    print(f'#{case} {ans}')