import sys
# 주어지는 수를 담는 배열 lst
lst = [int(sys.stdin.readline()) for _ in range(5)]
# lst을 정렬
lst.sort()
# 평균을 출력
print(sum(lst)//5)
# 중앙값을 출력
print(lst[2])