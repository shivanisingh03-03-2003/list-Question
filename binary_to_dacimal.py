# bainary to decimal

# list=[1,0,0,1,1,0,1,1]

# i=0
# s=0
# sum=0
# while i<len(list):
#     m=list[i]
#     s=(2**i)*m
#     i=i+1
#     sum+=s
# print(sum)


# list=[1,0,0,1,0,0,1]
# i=0
# s=0
# sum=0
# n=6
# while i<len(list):
#     m=list[i]
#     s=(2**i)*m
#     n=n-1
#     i=i+1
#     sum+=s
# print(sum)


list=[1,0,0,1,1,0,1,1]
i=0
s=0
sum=0
lenght=len(list)-1
while i<len(list):
    m=list[lenght]
    s=(2**i)*m
    lenght=lenght-1
    i=i+1
    sum+=s
print(sum)                                             
