input()
M = set(map(int, input().split()))
input()
N = set(map(int, input().split()))

for i in sorted(list(M.symmetric_difference(N))):
    print(i)

    

    

    
