# Palindrome wo strings ya numbers hote hai jo ulta seedhe same hote hai. Jaise, NITIN. Nitin ko aap left se padho ya right se, nitin hi hai. Aise hi MOM bhi 
# ek palindrome hai. Code likho jo check kare ki kya list palindrome hai ya nahi. Aur print karo “Haan! palindrome hai” agar hai. Aur “nahi! Palindrome nahi 
# hai” agar nahi hai. Abhi ke liye iss list ko use kar ke code likh sakte ho:


# name=[ "1","2","1" ,"2"] 
# i=0
# n=-1
# while i<len(name):
#     m=name[i]
#     a=name[n]
#     if m==a:
#         n=n-1
#         b=name
    
#     else:
#         print("not palindrome")
#         break
#     i=i+1
#     print(b,"it is plindrome")
#     break


name=[ 'n', 'i', 't', 'i', 'i' ] 
i=0
n=-1
while i<len(name):
    m=name[i]
    a=name[n]
    if m==a:
        n=n-1
        print("it is palindrome")
    else:
        print(" not")
    i=i+1