# Humei char_list mei jo bhi characters hai, unki occurences count karni hai, aur ek nested list mei 
# save karni hai, phir uss nested list ko use kar kar jo output hai, woh print karna hai.

# char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# i=0
# new=[]
# while i<len(char_list):
#     j=0
#     count=0
#     while j<len(char_list):
#         if char_list[i]==char_list[j]:
#             count = count+1
#         j+=1
#     new.append(count)
#     new.append(char_list[i])
#     i=i+1
# print(new)

char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
new=[]
while i<len(char_list):
    j=0
    count=0
    while j<len(char_list):
        if char_list[i]==char_list[j]:
            count = count+1
        j+=1
    if char_list[i]in new:
        i+=1
        continue
    new.append(char_list[i])
    print(char_list[i],"are",count)
    # i=i+1
print(new)                                                                                                                                                                                                                             
