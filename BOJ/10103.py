n = int(input())

player1_score, player2_score = 100, 100

for _ in range(n):
    player1, player2 = map(int, input().split())

    if player1 < player2:
        player1_score -= player2
    elif player2 < player1:
        player2_score -= player1

print(player1_score)
print(player2_score)