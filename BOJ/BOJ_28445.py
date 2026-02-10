import sys

# 아빠, 엄마 새의 색을 저장하는 셋 colors
colors = set()

for _ in range(2):
    C1, C2 = sys.stdin.readline().rstrip().split()
    colors.add(C1)
    colors.add(C2)

colors = sorted(list(colors))

for c1 in colors:
    for c2 in colors:
        print(c1, c2)