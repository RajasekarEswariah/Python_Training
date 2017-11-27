Data = input()
b =list(Data)

even = []
odd = []

for a in b:
  c = int(a)

  if c % 2 == 0:
    even.append(c)
  else:
     odd.append(c)

print ("Even numbers is {}".format(even))
print("Odd numbers is {}".format(odd))
