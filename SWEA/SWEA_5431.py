import sys
sys.stdin = open('sample_input.txt')

# 테스트 케이스 수 T
T = int(input())
for case in range(1, T+1):
    # 수강생 수 N, 과제 제출 수강생 수 K
    N, K = map(int, input().split())
    # 과제 제출 수강생의 번호
    done = list(map(int, input().split()))
    # 모든 수강생의 번호를 담은 리스트 lst
    lst = [x for x in range(1,N+1)]

    # 과제 제출한 수강생의 모든 번호를 lst에서 제거
    for d in done:
        lst.remove(d)
    # 테스트 케이스 번호와 미제출 수강생 번호 출력
    print(f'#{case}',*lst)