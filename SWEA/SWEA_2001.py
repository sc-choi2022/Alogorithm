import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수
test_case = int(input())
for case in range(1, test_case + 1):
    # N*N 파리 영역, M*M 파리채 크기
    N, M = map(int, input().split())
    # 각 위치의 파리 수 정보
    fly_arr = [list(map(int, input().split())) for _ in range(N)]
    # 최대 수 초기화
    max_sum = 0

    # N*N배열에서 M*M크기의 파리채를 사용하는 모든 경우에서
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            # 각 횟수마다의 파리 수 temp_sum을 0으로 초기화
            temp_sum = 0
            # 파리채의 크기만큼 잡은 파리 수 개산
            for ii in range(M):
                for jj in range(M):
                    temp_sum += fly_arr[i + ii][j + jj]
            # 현재 잡은 파리수와 최대 수 비교
            if max_sum < temp_sum:
                max_sum = temp_sum
    # 테스트 케이스 번호와 최대 파리수 출력
    print(f'#{case} {max_sum}')