# Code likho jo neeche di gayi lists ke items ko reverse order yaani ki ulta print kare.

places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"] 
length=len(places)
i=0
while i<length:
    print(places[i])
    i=i-1
print(places)


# length=len(places)-1
# while length>0:
#     print(places[length])
#     length=length-1


# l=len(places)
# s=""
# while l>0:
#     s+=places[l-1]
#     l-=1
# print(s)




list1=[10,20,30,40]
list2=[100,200,300,400]
# i=0
# lenght=len(list2)
# while i<len(list1):
#     j=-1
#     while len(list2)>j:
#         j=j+1
#     lenght=lenght-1
#     print(list1[i],list2[lenght])
#     i+=1
    
    
i=0
j=len(list2)-1
while i<len(list1):
    print(list1[i],list2[j])
    j-=1
    i+=1



a=["hello","ok"]
b=["sir","take"]
c=[]
i=0
while i<len(a):
    j=0
    while j<len(a):
        c.append(a[i]+b[j])
        j=j+1
    i=i+1
print(c)
    