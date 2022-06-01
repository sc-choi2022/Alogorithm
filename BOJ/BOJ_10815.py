# 상근이가 가진 숫자 카드의 개수 N
N = int(input())
# 상근이가 가진 카드의 N개의 숫자를 담을 리스트 numberN
numberN = list(map(int,input().split()))
# 존재 여부를 확인할 카드의 개수 M
M = int(input())
# M개의 카드의 숫자들을 담을 리스트 numberM
numberM = list(map(int,input().split()))
# 0혹은 1을 출력할 리스트 ans
# ans = [0] * M
ans = ''
for i in range(len(numberM)):
    if binary(numberN, numberM[i], 0, N-1)

print(ans)