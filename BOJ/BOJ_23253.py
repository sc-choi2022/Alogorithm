import sys

# 교과서의 수 N, 교과서 더미의 수 M
N, M = map(int, sys.stdin.readline().split())
# 올바른 순서대로 교과서를 꺼내는 여부를 저장하는 변수 flag
flag = True

for _ in range(M):
    # 더미에 쌓인 교과서의 개수 cnt
    cnt = int(sys.stdin.readline())
    # 교과서의 번호를 저장하는 배열 dummy
    dummy = list(map(int, sys.stdin.readline().split()))

    for i in range(cnt-1):
        # 더미가 오름차순이 아닌 경우
        if dummy[i] < dummy[i+1]:
            dummy = False
            break
    # 불가능한 경우
    if not flag:
        break

# 올바른 순서대로 교과서를 꺼낼 수 있다면 Yes를, 불가능하다면 No를 출력
print('Yes' if flag else 'No')