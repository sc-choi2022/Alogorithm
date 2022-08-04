import sys
# 버거의 가격을 담을 리스트 burger, 음료 가격을 담을 리스트 drink
burger = [int(sys.stdin.readline()) for _ in range(3)]
drink = [int(sys.stdin.readline()) for _ in range(2)]
# 가장 싼 세트 메뉴의 가격을 출력
print(min(burger) + min(drink) -50)