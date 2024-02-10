# 날짜 수 N, 연속 날짜 수 K
N, K = map(int, input().split())
arr = list(map(int,input().split()))
lst = [sum(arr[:K])]

# 모든 연속 날짜수의 첫날에 대해서
for i in range(N-K):
    # 이전 더해진 것의 첫번째 값을 빼고 뒤에 값을 추가
    temp = lst[i] - arr[i] + arr[K+i]
    # 모든 더한 값을 lst에 추가
    lst.append(temp)
# 가장 큰 값 출력
print(max(lst))


import sys

# 날짜 수 N, 연속 날짜 수 K
N, K = map(int, sys.stdin.readline().split())
# 온도를 저장하는 배열 temperature
temperature = list(map(int, sys.stdin.readline().split()))

# 온도의 합이 최대가 되는 값 answer
answer = sum(temperature[:K])
tmp = answer

for i in range(N-K):
    answer = max(answer, tmp)
    tmp -= temperature[i]
    tmp += temperature[K+i]

# 온도의 수열에서 연속적인 K일의 온도의 합이 최대가 되는 값을 출력
print(max(answer, tmp))