n = input()
score = list(map(int, input().split()))
max_score = max(score)
sum = sum(score)
print(sum*100/max_score/int(n))