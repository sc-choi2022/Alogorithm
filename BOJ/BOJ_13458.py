# 시험장의 개수 N
N = int(input())
# 응시자의 수를 담을 리스트 A
A = list(map(int, input().split()))
# 총감독관의 가능 감시수 B, 부감독관의 가능 감시수 C
B, C = map(int, input().split())

# ans을 0으로 초기화
ans = 0
for i in range(len(A)):
    # i시험장의 응시자수 number
    number = A[i]
    temp = 1000000
    # 총감독관이 모두 감시 가능한 경우
    if number <= B:
        temp = 1
    # 총감독과 부감독이 응시자수만큼 감시가능한 경우
    elif (number-B)%C==0:
        temp = min(temp, (number-B)//C + 1)
    # 그 외의 경우
    else:
        temp = min(temp, (number-B)//C + 2)
    ans += temp
# ans을 출력
print(ans)