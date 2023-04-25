from collections import defaultdict
import sys

# 나무 종의 이름과 그루수를 저장할 딕셔너리 trees
trees = defaultdict(int)
# 총 그루수를 저장할 변수 cnt
cnt = 0
while True:
    tree = sys.stdin.readline().rstrip()
    if not tree:
        break
    trees[tree] += 1
    cnt += 1
# trees의 모든 나무의 종을 사전순으로 정렬
names = sorted(list(trees.keys()))
# 정렬된 나무의 종과 차지하는 비율을 백분율로 소수점 4째자리까지 반올림해 함께 출력
for name in names:
    print('%s %.4f' %(name, trees[name]/cnt * 100))