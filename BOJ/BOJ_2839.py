# 설탕 무게 N
N = int(input())
# 최소가능 봉지 less값 N//5로 초기화
less = N//5
# 출력할 답 ans 0으로 초기화
ans = 0

for i in range(less, -1, -1):
    # ans와 temp에 i와 N - 5*i 저장
    ans = i
    temp = N - 5*i
    # temp가 0인 경우
    if temp == 0:
        print(ans)
        break
    # temp가 3의 배수인 경우
    elif temp%3 == 0:
        ans += temp//3
        print(ans)
        break
# 위 경우에 속하지 않은 경우
else:
    print(-1)