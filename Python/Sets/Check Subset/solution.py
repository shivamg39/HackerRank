for times in range(int(input())):
    input()
    A = set(map(int, input().split()))
    input()
    B = set(map(int, input().split()))
    subSet = True
    for num in A:
        if num not in B:
            subSet = False
    print(subSet)

    

    

    

    
