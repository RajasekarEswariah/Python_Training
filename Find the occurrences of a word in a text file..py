import os

s= open(os.path.realpath("../test")).read()
print (s)
x= s.split(' ')
count =dict()
for letter in x:
 if letter in count:
   count[letter] +=1
 else:
   count[letter] =1


print(count)
