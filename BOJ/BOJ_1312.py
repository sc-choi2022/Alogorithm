# 피제수(분자) A, 제수(분모) B, 구할 소숫점 아래 N번째 자리수
A, B, N = map(int, input().split())

# 기준이 될 나머지를 A에 할당하기 위한 for문
for i in range(N):
    if i == 0:
        A = A%B
    else:
        A = (A*10)%B
# 나머지를 기준으로 몫의 소수점 아래 N번째 자리수를 출력
print((A*10)//B)