import sys

# 동전의 종류 N개, 만들고자 하는 합 K
N, K = map(int, sys.stdin.readline().split())

# 동전의 가치를 담을 리스트 coins에 동전의 가치를 내림차순으로 담는다.
coins = [0]*N
for i in range(N-1, -1, -1):
    coins[i] = int(sys.stdin.readline())

# 출력할 필요한 동전 개수를 세는 변수 ans
ans = 0
# 가장 큰 수 부터 사용하여 동전의 개수를 센다.
idx = 0
# K가 0이 될 때까지 진행
while K:
    # K를 coins[idx]의 값으로 나누었을 때 몫이 있다면
    # ans와 K 값을 재설정
    if K // coins[idx]:
        ans += K // coins[idx]
        K = K % coins[idx]
    # idx를 변경
    idx += 1
# ans 출력
print(ans)