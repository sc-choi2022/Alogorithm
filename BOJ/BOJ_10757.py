# 두 수를 string타입으로 변수 a,b에 할당한다.
a, b = input().split()
# a, b의 각 문자로 이루어진 lst1, lst2 리스트를 생성한다.
lst1 = list(a)
lst2 = list(b)
# list1, lst2의 길이를 확인하여 길이를 맞춰준다.
if len(lst1) > len(lst2):
    lst2 = ['0']*(len(lst1) - len(lst2)) + lst2
else:
    lst1 = ['0'] * (len(lst2) - len(lst1)) + lst1
# 정답 ans를 0으로 초기화
ans = 0
# lst1,2의 길이 만큼 진행 각 자리에서 계산 후 10의 제곱을 고려하여 ans에 더해준다.
for i in range(len(lst1)):
    temp = int(lst1[-i-1]) + int(lst2[-i-1])
    ans += temp*10**i
# ans 출력
print(ans)