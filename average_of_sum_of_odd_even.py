# Ek code likho jo kissi bhi list ke liye uss list ke do average ko output karta hai, ki uss list mei 
# odd numbers ka average aur even numbers ka average kitna hai.
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
sum=0
even=0
odd=0
o=0
while i<len(elements):
    if elements[i]%2==0:
        sum=sum+elements[i]
        even+=1
    else:
        odd=odd+(elements[i])
        o+=1
    i=i+1
print(sum//even)  
 #4 even number
print(odd//o)    
#7 odd numbers



        
