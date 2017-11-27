import os

s= open(os.path.realpath("../test")).read()

x= s.split(' ')
words= {"a","an","The","if","of" }

count =dict()
for letter in x:
    if letter not in words:

        if letter in count:
            count[letter] +=1
        else:
            count[letter] =1


print(count)
