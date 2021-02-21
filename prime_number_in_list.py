
n=[1,2,7,3,4,8,13,17,19,26,44,15,11,7,5,6,55]
i=0
a = []
b = []
while i<len(n):
    count=0
    k=2
    while k<n[i]:
        if n[i]%k==0:
            count+=1
        k+=1
    if count==0:
        # print(n[i],"Prime")
        a.append(n[i])
    else:
        # print(n[i],"Not Prime")
        b.append(n[i])
    i+=1
print(a)
print(b)
        
    
