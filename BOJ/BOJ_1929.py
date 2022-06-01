# 소수를 확인해 줄 함수 primenumber
def primenumber(number):
    # number가 1인 경우 소수가 아니다
    if number == 1:
        return False
    else:
        # 2부터 number의 제곱근까지의 수
        for i in range(2, int(number**0.5) + 1):
            # number가 i로 나눠진다면 소수가 아니다
            if number % i == 0:
                return False
        # if문에 걸리지 않으면 소수이다.
        return True

# 자연수 M, N
M, N = map(int, input().split())

for number in range(M, N + 1):
    # primenumber함수에서 True가 return 되면 number를 출력한다.
    if primenumber(number):
        print(number)