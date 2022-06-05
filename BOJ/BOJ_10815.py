# 상근이가 가진 숫자 카드의 개수 N
N = int(input())
# 상근이가 가진 카드의 N개의 숫자를 담을 리스트 numberN
numberN = set(map(int,input().split()))
# 존재 여부를 확인할 카드의 개수 M
M = int(input())
# M개의 카드의 숫자들을 담을 리스트 numberM
numberM = list(map(int,input().split()))

# 상근이의 M개의 카드가
for i in range(M):
    # numberN에 포함되어 있다면 1과 공백을 출력하고
    if numberM[i] in numberN:
        print(1, end=' ')
    # 포함되어 있지 않다면 0과 공백을 출력한다.
    else:
        print(0, end=' ')