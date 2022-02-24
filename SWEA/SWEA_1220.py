import sys
sys.stdin = open('input.txt')

for case in range(1, 10+1):
    # 한 변의 길이
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 교착 수 초기화
    cnt = 0

    # 1: N극 2: S극
    for j in range(N):
        # 각 단계마다 열을 담을 리스트 temp
        temp = []
        # 현재의 시작위치를 저장할 now 변수 초기화
        now = 0
        # arr의 각 열의 값들을 확인하여
        for i in range(N):
            # 값이 1이고 현재 시작위치가 초기화 값 0이라면
            if arr[i][j] == 1 and now == 0:
                # 시작위치 1로 할당
                now = 1
            # 값이 2이고 현재 시작위치가 1이라면 교착이 생기므로
            elif arr[i][j] == 2 and now == 1:
                # now를 초기화
                now = 0
                # 교착 수 1 증가
                cnt += 1
    # 테스트 케이스의 번호와 교착 상태의 개수 출력
    print(f'#{case} {cnt}')