import sys

def check():
    # 범위 내 학생 수 cnt
    cnt = 0
    for k in range(min(R, R1), max(R, R1)+1):
        for l in range(min(C, C1), max(C, C1)+1):
            if classroom[k][l] == 1:
                cnt += 1
    # 조건에 만족하는 경우 1 return
    if (R1-R)**2 + (C1-C)**2 >= 25 and cnt >= 3:
        return 1
    # 조건에 만족하지 않는 경우 0 return
    else:
        return 0

# 자연수 N
N = int(sys.stdin.readline())
# 0: 빈 자리, 1: 성규가 아닌 학생, 2: 성규, 5: 교수님
classroom = [[] for _ in range(N)]
# 성규의 위치 R, C, 교수님의 위치 R1, C1
R, C, R1, C1 = 0, 0, 0, 0

for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if lst[j] == 2:
            R, C = i, j
        elif lst[j] == 5:
            R1, C1 = i, j
    classroom[i] = lst
# 성규가 교수님에게서 도망칠 수 있으면 1, 그렇지 못하면 0을 출력
print(check())