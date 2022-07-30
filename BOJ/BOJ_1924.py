# 요일을 담은 리스트 days
days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

# idx에 대응하는 월의 일수를 담을 for문
months = [0]*13
for i in range(13):
    if i == 2:
        months[i] = 28
    elif i in (4, 6, 9, 11):
        months[i] = 30
    else:
        months[i] = 31
# x월 y일의 값을 x, y에 저장
x, y = map(int, input().split())
# 주어지는 날짜의 총 일수를 담을 변수 ans을 초기화
ans = 0
# ans에 월에 따른 일수를 더하는 for문
for i in range(1, x):
    ans += months[i]
# y일을 더한다.
ans += y
# 요일을 구하여 출력
print(days[ans%7])