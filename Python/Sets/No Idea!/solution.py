size = input()

n = list(input().split())
a = set(input().split())
b = set(input().split())

score = 0
for num in n:
    if num in a:
        score += 1
    elif (num in b):
        score -= 1
print(score)
