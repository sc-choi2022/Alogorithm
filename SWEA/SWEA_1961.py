import sys

sys.stdin = open('input.txt')

# 테스트 케이스의 개수 T
T = int(input())
for case in range(1, T + 1):
    # N x N 행렬 N
    N = int(input())
    # N x N 행렬을 담은 리스트 arr
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 90, 180, 270 회전한 값을 넣어줄 리스트 초기ㅘ
    arr_90 = [[0] * N for _ in range(N)]
    arr_180 = [[0] * N for _ in range(N)]
    arr_270 = [[0] * N for _ in range(N)]

    # 행과 열을 규칙에 맞춰 arr_90, arr_180, arr_270 리스트에 할당
    for i in range(N):
        for j in range(N):
            arr_90[i][j] = arr[-j - 1][i]
            arr_180[i][j] = arr[-i - 1][-j - 1]
            arr_270[i][j] = arr[j][-i - 1]
    # 케이스 번호 출력
    print(f'#{case}')
    # 회전된 리스트에 들어있는 모든 리스트에 대해
    for ii in range(len(arr)):
        # 각 값을 붙여서 출력
        # 한 리스트가 끝나면 띄어쓰기로 구분
        # 90도 회전 리스트
        for ar90 in arr_90[ii]:
            print(ar90, end='')
        print(' ', end='')
        # 180도 회전 리스트
        for ar180 in arr_180[ii]:
            print(ar180, end='')
        print(' ', end='')
        # 270도 회전 리스트
        for ar270 in arr_270[ii]:
            print(ar270, end='')
        print(' ', end='')
        print()