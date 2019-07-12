def average(array):
    arr = set(array)
    avg = 0
    for num in arr:
        avg += num
    return avg / len(arr)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

    

    

    

    

    
