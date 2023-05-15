import sys

# 월별 딕셔너리
month = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6,
         'July':7, 'August':8, 'September':9, 'October':10, 'November':10, 'December':12}
day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total = 365*24*60
number = 0
date = list(sys.stdin.readline().rstrip().replace(',','').replace(':',' ').split())
for i in range(5):
    if i == 0:
        for j in range(1, month[date[i]]):
            number += day[j]

    elif i == 1:
        number += int(date[i]) - 1
        number *= 24*60
    elif i == 2:
        continue
    elif i == 3:
        number += int(date[i])*60
    else:
        number += int(date[i])
print(number / total * 100)