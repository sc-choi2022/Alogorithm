import sys

# 테스트 케이스의 수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 한문장의 단어의 수 N
    N = int(sys.stdin.readline())
    # 공개키 PK1, PK2
    PK1 = sys.stdin.readline().rstrip().split()
    PK2 = sys.stdin.readline().rstrip().split()
    # 공개키 PK2에 따른 PK1의 위치를 저장하는 배열 idxs
    idxs = [0]*N

    for i in range(N):
        idxs[i] = PK2.index(PK1[i])

    # 암호문 words
    words = sys.stdin.readline().rstrip().split()
    # 암호문을 해독한 평문 출력
    for j in range(N):
        print(words[idxs[j]], end=' ')
    print()