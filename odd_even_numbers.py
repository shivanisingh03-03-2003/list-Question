# Ek code likho jo kisi bhi list ke liye yeh output karta hai, ki uss list mei kitne odd numbers hai aur kitne even numbers hai.



elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
o=[]
e=[]
while i<len(elements):
    if elements[i]%2==0:
        e.append(elements[i])
    else:
        o.append(elements[i])
    i=i+1
print(o)
print(e)

# for printing how much number is odd or even 
# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
# i=0
# odd=0
# even=0
# while i<len(elements):
#     if elements[i]%2==0:
#         even+=1
#     else:
#         odd+=1
#     i=i+1
# print("odd",odd)
# print("even",even)





          

       