import sys

month, day, year, time = sys.stdin.readline().replace(',', '').split()
day, year = int(day), int(year)
hour, minute = map(int, time.split(':'))

month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 윤년인 경우
if not year%400 or (not year%4 and year%100):
    day_list[1] += 1
total = sum(day_list) * 24 * 60
now = (sum(day_list[:month_list.index(month)]) + day-1)*24*60 + 60*hour + minute
# 이번 해가 몇%지났는지 출력
print(now/total*100)