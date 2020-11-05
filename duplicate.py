arr1= [1 , 2, 4, 7, 9, 8, 2]
arr2= [3, 4, 1, 8 ,10, 3]
uniqDict = {}

for i in arr1: 
    if uniqDict.get(i):
         pass
    else: 
         uniqDict[i]=1
for j in arr2: 
    if uniqDict.get(j):
         pass
    else: 
         uniqDict[j]=1
         
res = list(uniqDict.keys())
print(res)
res.sort()
print(res)
