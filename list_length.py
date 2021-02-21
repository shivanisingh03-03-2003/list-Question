# Aapko aisa program likhna hai, jo kisi bhi list ko le kar us mei kitne elements hai, yeh batata hai. Yeh len() function jaisa hai, isliye hum iss program ko 
# implement karte hue len() function ka use nahi karenge balki yeh samjhenge ki kisi programmer ne len() function kaise implement kiya hoga.

 


# how to find how mach list have element.
# number=[50,40,23,70,56,12,5,10,7]
# i=number.index(number[-1])+1
# print(i)

number=[50,40,23,70,56,12,5,10,7]
count=0
while number[count:]:
    count=count+1
print(count)
    

# number=[50,40,23,70,56,12,5,10,7]
# i=0
# count=0
# while i<len(number):
#     count+=1
#     i+=1
# print(count)



# Ab hum while loop ka use kar ek ek kar ke apna counter bada sakte hain aur iss list ka ek ek element access kar sakte hain. Jaise:


# students_list = ["robin", "anamika", "faisal", "valmiki", "waseem", "amara"]
# list_length = len(students_list)
# index = 0
# while index < list_length:
#     print (students_list[index])
#     index = index + 1 







