# Code likho jo iss list mein se maximum dhund kar ke print kare.


# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7] 
# i=0
# sum=0
# while i<len(numbers):
#     sum+=(numbers[i])
#     i=i+i
# print(sum)


numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7] 
i=0
sum=numbers[i]
while i<len(numbers):
    j=numbers[i]
    if j>sum:
        sum=j
    i=i+1
print(sum)











