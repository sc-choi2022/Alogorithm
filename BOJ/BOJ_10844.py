# 계단 수 길이 N
N = int(input())
# N == 1일때 0으로 시작하는 수는 계단수를 제외
# 계단수의 마지막 수를 인덱스로 개수를 담아주는 리스트 number
number = [0] + [1]*9

# 초기 1개의 개수를 제외하고 N-1번 계단수를 구한다.
for _ in range(N-1):
    # 다음 계단수를 담을 리스트 dp
    dp = [0] * 10
    for i in range(9+1):
        # 이전 계단수의 마지막 자리가 0인 경우
        if i == 0:
            dp[i+1] += number[i]
        # 마지막 자리가 9인 경우
        elif i == 9:
            dp[i-1] += number[i]
        # 그 외의 경우
        else:
            dp[i-1] += number[i]
            dp[i+1] += number[i]
    # number을 dp로 갱신
    number = dp
# 정답을 1,000,000,000으로 나눈 나머지를 출력
print(sum(number)%1000000000)