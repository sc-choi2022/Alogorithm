import sys
# 숫자의 영문명을 저장하는 딕셔너리 numbers
numbers = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'zero'}
# 숫자의 범위 기준 M이상 N이하
M, N = map(int, sys.stdin.readline().split())
# 범위 안의 숫자의 영어를 저장하는 배열 align
align = []

for i in range(M, N+1):
    S = str(i)
    num = ''
    for s in S:
        num += numbers[s]
    align.append((num, i))
# 사전순으로 정렬
align.sort(key=lambda x:x[0])

# M 이상 N 이하의 정수를 문제 조건에 맞게 정렬하여 한 줄에 10개씩 출력
for j in range(1, len(align)+1):
    print(align[j-1][1], end=' ')
    if j%10 == 0:
        print()