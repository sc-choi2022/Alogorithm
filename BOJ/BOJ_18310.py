# 집의 수 N
N = int(input())
# 아파트의 위치를 담은 리스트 location
location = list(map(int,input().split()))
# 위치를 정렬
location.sort()
# 아파트의 위치 중 가운데 값(두개라면 작은 값)을 기준으로 설치하면
# 안테나로부터 모든 집까지의 거리의 총 합이 최소가 되도록 설치할 수 있다.
# 따라서 N-1//2의 위치를 출력
print(location[(N-1)//2])