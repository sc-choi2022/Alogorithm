import sys

# 아빠, 엄마 새의 색을 저장하는 셋 colors
colors = set()

for _ in range(2):
    # 부모 새의 몸통 색과 꼬리 색 C1, C2
    C1, C2 = sys.stdin.readline().rstrip().split()
    colors.add(C1)
    colors.add(C2)

colors = sorted(list(colors))

# 자식 새의 몸통 색과 꼬리 색의 쌍을 한 줄에 하나씩 사전 순으로 출력
for c1 in colors:
    for c2 in colors:
        print(c1, c2)