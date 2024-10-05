import sys

def find():
    for i in range(N-1, -1, -1):
        for j in range(N-1):
            # U[i]이 최적해 인 경우 출력
            if U[i]-U[j] in A:
                print(U[i])
                return

# 자연수의 개수 N
N = int(sys.stdin.readline())
# 집합 U의 원소를 저장하는 배열 U
U = sorted(list(int(sys.stdin.readline()) for _ in range(N)))

# 집합 U의 두개 원소의 합을 저장하는 셋 A
A = set()

for u1 in U:
    for u2 in U:
        A.add(u1+u2)

find()