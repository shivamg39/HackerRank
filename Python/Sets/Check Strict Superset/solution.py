arr = set(map(int, input().split()))
s = 0
for i in range(int(input())):
    arr1 = set(map(int, input().split()))
    if arr.issuperset(arr1) != True:
        s = 1
if s == 1:
    print(False)
else:
    print(True)
    

    

    
    

    

    
    

    
