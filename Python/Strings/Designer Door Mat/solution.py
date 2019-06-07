# Enter your code here. Read input from STDIN. Print output to STDOUT

height, width = [int(n) for n in input().split(' ')]

for row in range(1, height, 2):
    print(('.|.'*row).center(width, '-'))

print('WELCOME'.center(width, '-'))

for row in reversed(range(1, height, 2)):
    print(('.|.'*row).center(width, '-'))
