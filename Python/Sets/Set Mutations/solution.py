input()
A = set(map(int, input().split(" ")))

for times in range(int(input())):
    command, size = input().split(" ")
    N = set(map(int, input().split(" ")))

    if (command == "intersection_update"):
        A.intersection_update(N)
    elif (command == "update"):
        A.update(N)
    elif (command == "difference_update"):
        A.difference_update(N)
    elif (command == "symmetric_difference_update"):
        A.symmetric_difference_update(N)

sum = 0
for num in A:
    sum += num

print(sum)




