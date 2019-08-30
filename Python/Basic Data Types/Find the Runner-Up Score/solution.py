if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    high = -101
    shigh = -101
    for num in arr:
        if (num > shigh):
            if (num < high):
                shigh = num
            elif (num > high):
                shigh = high
                high = num
    
    print(shigh)

    
    

    
