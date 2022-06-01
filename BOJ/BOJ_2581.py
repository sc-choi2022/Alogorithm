# 자연수 M, N
M = int(input())
N = int(input())
# M과 N 사이의 소수들을 담을 리스트 lst
lst = []

# M부터 N까지의 수를 확인한다.
for number in range(M, N+1):
    # 소수의 약수가 아닌 가장 작은 수 2를 시작으로
    cnt = 2
    #while문을 number값이 cnt보다 클 때 실행한다.
    while number > cnt:
        # 만약 cnt가 number의 약수이면 while문을 break
        if number % cnt == 0:
            break
        # if문에서 break하지 않았다면 cnt 1 증가
        cnt += 1
    # number와 cnt이 같다면 소수라는 의미이므로 lst에 추가한다.
    if number == cnt:
        lst.append(number)
# 소수가 없다면 -1 출력
if len(lst) == 0:
    print(-1)
# 소수가 있다면
else:
    # 소수들의 합을 출력
    print(sum(lst))
    # 소수 중 가장 작은 값을 출력
    print(lst[0])