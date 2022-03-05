# 1의 개수가 K개인 ans_cnt를 출력하는 함수
def cnt(arr, K):
    # 출력할 개수 ans_cnt 초기화
    ans_cnt = 0

    # arr의 각 행에 대해 연속된 1의 개수를 세고
    for ar in arr:
        # 각 행마다 1의 개수 cnt를 초기화
        cnt = 0
        # 행의 값들에서 1의 값을 확인 하여
        for i in range(len(ar)):
            # 1이라면 cnt 1 증가
            if ar[i] == 1:
                cnt += 1
            # 0이라면
            elif ar[i] == 0:
                #  K 길이가 되면 ans_cnt 1 증가
                if cnt == K:
                    ans_cnt += 1
                # cnt 초기화
                cnt = 0
        # 행의 마지막에 연속된 1의 길이가 K이 되면 ans_cnt 1 증가, cnt 초기화
        if cnt == K:
            ans_cnt += 1
    return ans_cnt


# 테스트 케이스의 개수 T
T = int(input())
for case in range(1, T + 1):
    # NxN 행렬의 N, 길이 K
    N, K = map(int, input().split())
    # N개 줄의 정보를 arr에 할당
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 행만을 검사하기 위해 arr의 전치행렬 trans_arr 생성
    trans_arr = list(map(list, zip(*arr)))

    # arr와 전치행렬 trans_arr의 연속된 1의 개수가 K개인 개수를 ans_cnt에 할당
    ans_cnt = cnt(arr, K) + cnt(trans_arr, K)

    # 테스트케이스 번호와 정답 출력
    print(f'#{case} {ans_cnt}')