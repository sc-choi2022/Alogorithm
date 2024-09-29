import sys

def cantoring(L, idx):
    # 선의 길이가 1인 경우 return
    if L == 1:
        return
    # 범위를 3등분한 길이 tri
    tri = L//3
    for i in range(idx+tri, idx+2*tri):
        A[i] = ' '
    cantoring(tri, idx)
    cantoring(tri, idx+2*tri)

while True:
    try:
        N = int(sys.stdin.readline())
        A = ['-'] * 3**N
        cantoring(3**N, 0)
        # 칸토어 집합의 근사를 출력
        print(''.join(A))
    except:
        break