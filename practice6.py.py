lst=[56789]
min_ele=lst[0]
max_ele=lst[0]
for i in range(len(lst)):
    if lst[i]<min_ele:
        min_ele=lst[i]
    elif lst[i] > max_ele:
        min_ele = lst[i]
print(min_ele)
print(max_ele)

lst=[15,20,35,40,75,60,30,90]
biggest_num=None
for num in range(len(lst)):
    if num%2==0:
        if num>biggest_num:
            biggest_num=num
print(biggest_num)

#biggest even
numbers = [3, 7, 2, 8, 5, 10, 11]

lst=[3,7,2,8,5,10,11]
big_even=0
for i in lst:
    if i%2==0 and i>big_even:
        big_even=i
print(big_even)

#binary search
lst=[1, 0, 0, 1]
for i in range(len(lst)):
    for j in range(0, len(lst)-i-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
print(lst)

#Move all negative elements to end
lst=[-5, 7, -3, -4, 9, 10, -1, 11]
neg=[]
pos=[]
result=[]
for i in lst:
    if i<=0:
        neg.append(i)
    else:
        pos.append(i)
        result=pos+neg
print(result)

#search 2D matrix
lst = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 34
found=False
for i in lst:
    for j in range(len(i)):
        if target==i[j]:
            found=True
            break
if found:
    print("true")
else:
    print("false")