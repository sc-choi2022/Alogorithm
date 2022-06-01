# 소인수분해를 할 정수 N
N = int(input())
NN = N
# 소인수분해가 끝났는지 확인하기 위한 변수 check
check = 1
# 소인수분해 결과를 담을 리스트 lst
lst = []

# 2부터 N까지의 수
for number in range(2, N+1):
    while True:
        # N과 동일한 수인 NN을 나누면서 소인수분해를 진행한다.
        # number가 NN의 약수가 아니라면 break
        if NN % number != 0:
            break
        # number가 NN의 약수이면 NN을 나눠주고 lst에 인수를 추가
        NN //= number
        lst.append(number)
        # check는 number를 곱해준다.
        check *= number
    # check가 N이 되었다면 소인수분해가 끝난 것
    if check == N:
        break
# lst의 모든 값을 형식에 맞게 출력
for l in lst:
    print(l)