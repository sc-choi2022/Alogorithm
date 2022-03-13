# 날짜 수 N, 연속 날짜 수 K
N, K = map(int, input().split())
arr = list(map(int,input().split()))
add = [sum(arr[:K])]

# 모든 연속 날짜수의 첫날에 대해서
for i in range(N-K):
    # 이전 더해진 것의 첫번째 값을 빼고 뒤에 값을 추가
    temp = add[i] - arr[i] + arr[K+i]
    # 모든 더한 값을 add에 추가
    add.append(temp)
# 가장 큰 값 출력
print(max(add))