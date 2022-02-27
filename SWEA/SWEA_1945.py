import sys
sys.stdin = open('input.txt')

# 테스트 케이스의 개수 T
T = int(input())
for case in range(1, 1+T):
    # 숫자 N
    N = int(input())
    # 약수의 모든 종류를 담은 리스트 div
    div = [2, 3, 5, 7, 11]
    # 모든 약수의 종류의 개수를 담을 리스트 ans
    ans = [0]*5
    # 약수의 모든 종류에 대해 확인하기 위한 for문
    for i in range(len(div)):
        # 나눈 후 나머지의 값 temp
        temp = 0
        # temp가 약수인 경우 temp = 0일 때 증가시킬 temp_cnt값 초기화
        temp_cnt = 0
        while True:
            # 약수로 나눈 나머지 temp
            temp = N%div[i]
            # temp가 약수인 경우 temp = 0일 때
            if temp == 0:
                # temp_cnt 1 증가
                temp_cnt += 1
                # 나눈 후의 N 재설정
                N = N//div[i]
            # temp가 약수가 아닌 temp != 0일 때
            elif temp != 0:
                # ans에 나눈 수를 할당후 탈출
                ans[i] = temp_cnt
                break
    # 테스트케이스 번호 리스트 ans값을 출력
    print(f'#{case}', *ans)