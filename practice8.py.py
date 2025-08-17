lst=[0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
for i in range(0, len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i]>lst[j]:
            lst[i],lst[j]=lst[j],lst[i]
print(lst)

def equilibrium_index(lst):
    total_sum=0
    for num in lst:
        total_sum+=num
    left_sum=0
    for i in range(len(lst)):
        right_sum=total_sum-left_sum-lst[i]
        if left_sum==right_sum:
            return i
        left_sum+=lst[i]
    return -1

lst=[1, 1, 1, 1]
print(equilibrium_index(lst))

lst=[-7, 1, 5, 2, -4, 3, 0]
total_sum=0
for num in lst:
    total_sum+=num
left_sum=0
found = False
for i in range(len(lst)):
    right_sum=total_sum-left_sum-lst[i]
    if left_sum==right_sum:
        print(i)
        found=True
        break
    left_sum+=lst[i]
if not found:
    print(-1)

def peak_element(lst):
    for i in range(len(lst)):
        if lst[0] < lst[1] :
            return True
        else:
            return False
