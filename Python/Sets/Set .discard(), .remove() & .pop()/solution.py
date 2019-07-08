n = int(input())
s = set(map(int, input().split()))

for times in range(int(input())):
    commands = input().split()
    if (commands[0] == "pop"):
        s.pop()
    elif (commands[0] == "remove"):
        s.remove(int(commands[1]))
    elif (commands[0] == "discard"):
        s.discard(int(commands[1]))

total = 0
for num in s:
    total += num
print(total)



