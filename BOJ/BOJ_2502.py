import sys

# 할머니가 넘어온 날 D, 그 날 호랑이에게 준 떡의 개수 K
D, K = map(int, sys.stdin.readline().split())
# A와 B의 정보를 저장하는 배열 As, Bs
As, Bs = [0, 1] + [0] * (D-1), [0, 0, 1] + [0]*(D-2)

for i in range(3, D+1):
    As[i] = As[i-1] + As[i-2]
    Bs[i] = Bs[i-1] + Bs[i-2]

A, B = 0, Bs[D]
while True:
    if K%B == 0 and A:
        break
    A += 1
    K -= As[D]
# 첫 날에 준 떡의 개수 A를 출력
print(A)
# 둘째 날에 준 떡의 개수 B를 출력
print(K//Bs[D])