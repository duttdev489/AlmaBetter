#Remove item from tuple

tup = tuple(input().split(','))
item = input()
new_tup= list()
count=0
for  i in tup:
  if i != item:
    new_tup.append(i)
  elif i== item and count>=1:
    new_tup.append(i)
    count+=1
  else:
    count+=1
tup = tuple(new_tup)
print((tup))

#alternatively
tup.pop(item)
