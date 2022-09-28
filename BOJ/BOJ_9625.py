# 버튼을 누르는 횟수 K
K = int(input())
# i번 눌렀을 때 A, B의 개수를 각각 담을 dpA, dpB
dpA = [0]*46
dpB = [0]*46
# 초기화면 값을 dpA, dpB에 값으로 초기화
dpA[0], dpB[0] = 1, 0
for i in range(1, K+1):
    dpA[i] = dpB[i-1]
    dpB[i] = dpA[i-1] + dpB[i-1]
# A의 개수와 B의 개수를 공백으로 구분해 출력
print(dpA[K], dpB[K])