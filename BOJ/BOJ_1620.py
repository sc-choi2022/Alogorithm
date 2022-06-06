# 도감에 수록된 포켓몬 수 N, 문제의 수 M
N, M = map(int, input().split())

pokemon = {}

# 1부터 순서대로 딕셔너리 pokemon에 도감추가
for i in range(1, N + 1):
    pokemon[i] = input()
# value로 key를 찾기 위해 reverse_pokemon 딕셔너리 생성
reverse_pokemon = dict(map(reversed, pokemon.items()))

# M개의 input의 종류에 따라
for _ in range(M):
    question = input()
    # question이 정수라면 pokemon을 이용하여 출력
    if question.isdecimal():
        print(pokemon[int(question)])
    # question이 정수가 아니라면 reverse_pokemon을 이용하여 출력
    else:
        print(reverse_pokemon[question])