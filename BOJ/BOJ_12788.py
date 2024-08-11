import sys

# 회원수 N
N = int(sys.stdin.readline())
# 참가한 팀의 수 M, 팀을 구성하는데 필요한 팀원의 수 K
M, K = map(int, sys.stdin.readline().split())
# 각 회원들의 가지고 있는 펜의 수를 저장하는 배열 A
A = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

# 펜이 부족한 경우 STRESS 출력
if sum(A) < M*K:
    print('STRESS')
else:
    pencil = 0
    for i in range(N):
        pencil += A[i]
        # 빌린 회원의 수를 출력
        if pencil >= M*K:
            print(i+1)
            break