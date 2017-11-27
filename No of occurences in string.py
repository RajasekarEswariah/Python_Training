data = input()
x= data.split(' ')
count =dict()
for letter in x:
 if letter in count:
   count[letter] +=1
 else:
   count[letter] =1


print(count)





