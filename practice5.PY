lst=[1, 6, 11, 16, 21, 31]
for i in range(len(lst)):
    if lst[i+1]-lst[i]>5:
        print(lst[i]+5)
        break
# clockwise movement
lst=[9, 8, 7, 6, 4, 2, 1, 3]
rotate=[lst[-1]]+lst[:-1]
print(rotate)

#min and max
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
