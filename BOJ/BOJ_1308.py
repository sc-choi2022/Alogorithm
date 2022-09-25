from datetime import datetime
# 오늘의 날짜 년, 월, 일 y1, m1, d1
y1, m1, d1 = map(int, input().split())
# D-Day인 날의 날짜 년, 월, 일 y2, m2, d2
y2, m2, d2 = map(int, input().split())
# 천년 이상으로 긴 경우 gg를 출력
if y2-y1 > 1000 or (y2==y1+1000 and m2>=m1 and d2>=d1):
    print('gg')
else:
    # 남은 일수를 gap에 저장
    gap = datetime(y2, m2, d2) - datetime(y1, m1, d1)
    # D- 와 gap으로 출력
    print('D-'+str(gap.days))