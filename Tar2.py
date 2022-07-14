#Exercise number 1
#A
s = input("Please insert a string")
counts_dict = {}
for ch in s:
    counts_dict[ch] = counts_dict.get(ch,0) + 1
counts_dict

for key, value in sorted(counts_dict.items()):
    print(key, ' - ', value)
#B
new_dict = {}
for key, value in counts_dict.items():
   if value in new_dict:
       new_dict[value].append(key)
   else:
       new_dict[value]=[key]

print(new_dict)


#Exercise number 2
#A
lst1 = [11,  7, 5,  8, 5,  37,  11, 5] 
lst2 = [22, 8, 10, 1, 11]
lst3 = [ 71, 3, 22, 8, 2, 14, 1]
all = [lst1,lst2,lst3]
nodup = []
dup = []
print("The list with duplicates are: ")
for list in all:
    if len(list) != len(set(list)):
        print(list)
        i = set([x for x in list if list.count(x) > 1])
        print("list includes " + str(i) + " more than once")


    else:
        set(list)
        nodup.append(list)
#B
if len(nodup) == 0:
    print('The list is empty')
elif len(nodup) == 1:
    print("The common values are: "+str(nodup))
else:
    setmatches  = set.intersection(*map(set,nodup)) 
    print("The common values in the other lists: "+ str(setmatches))

#Exercise number 3
import numpy as np
lst4 = [31, 99, 3, 1943]
numbers = []
sr = []
for num1 in lst4:
 unique = [int(x) for x in set(str(num1))]
 sr.append(unique)
    
flat_list = []
for n in sr:
	for nm in n:
		flat_list.append(nm)
nw = np.unique(flat_list)
sort = input("In which order would you like the list? press 1 for escending or 2 ascending")
nw.sort()
if sort ==  '1':
    print(nw)
if sort == '2':
    print(nw[::-1])
