# iss lists mei se duplicates nikal kar, kisi aur list mei daal kar print karne hai.

n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11] 
new=[]
i=0
while i<len(n):
    if n[i]not in new:
        new.append(n[i])
    i=i+1
print(new)

