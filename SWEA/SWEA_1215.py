import sys
sys.stdin = open('input.txt')

for case in range(1,10+1):
    # 회문의 길이
    K = int(input())
    # 8x8 평면 글자판
    arr = [list(input()) for _ in range(8)]
    # arr의 전치행렬
    trans_arr = list(map(list,zip(*arr)))
    # 회문의 개수 초기화
    cnt = 0

    # 모든 행렬에 대해
    for i in range(8):
        # 길이 K만큼 slicing을 통해 잘라냄
        for j in range(8-K+1):
            # temp1는 arr, temp2는 trans_arr의 길이 K의 문자열을 담은 리스트
            temp1 = arr[i][j:j+K]
            temp2 = trans_arr[i][j:j+K]
            # temp1이 회문이라면 cnt 1증가
            if temp1 == temp1[::-1]:
                cnt += 1
            # temp2이 회문이라면 cnt 1증가
            if temp2 == temp2[::-1]:
                cnt += 1
    # 테스트케이스와 cnt 출력
    print(f'#{case} {cnt}')