input()
L = list(map(int, input().split()))
s1=set();
s2=set();
for num in L:
    if num in s1:
        s2.add(num)
    else:
        s1.add(num)

s3 = s1.difference(s2)

for num in s3:
    print(num)

    
