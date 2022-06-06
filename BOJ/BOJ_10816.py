# 상근이가 가진 카드의 개수 N
N = int(input())
# 상근이의 카드에 적힌 숫자 N개를 담은 S
S = list(map(int, input().split()))

# 시간 초과를 해결하기 위해 딕셔너리를 사용하여 상근이의 카드 정보를 저장한다.
dic = dict()
for s in S:
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

# 주어지는 숫자의 개수 M
M = int(input())
# M개의 숫자를 담은 리스트 G
G = list(map(int, input().split()))

# G의 모든 값들 중
for g in G:
    # dic에 있다면 g에 맞는 value값을 출력
    if g in dic:
        print(dic[g], end=' ')
    # dic에 없다면 0을 출력
    else:
        print(0, end=' ')