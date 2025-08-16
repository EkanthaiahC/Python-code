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

lst=[10, 20, 15, 2, 23, 90, 80]
print(peak_element(lst))

lst=[10, 10, 15, 2, 23, 90, 80]
for i in range(len(lst)):
    if lst[0] < lst[1] :
        print("True")
        break
    else:
        print("False")
        break


def transition_point(lst):
    for i in range(len(lst)):
        if lst[i]==1:
            return i
        i+=1
    return -1


lst=[1, 1, 1]
print(transition_point(lst))

lst=[0, 0, 0, 1, 1]
for i in range(len(lst)):
    if lst[i]==1:
        print(i)
        break
    else:
        print(-1)
        break

def subarraySum(arr, target):
    start = 0
    curr_sum = 0

    for end in range(len(arr)):
        curr_sum += arr[end]

        # Shrink only once per iteration if sum is too big
        if curr_sum > target:
            curr_sum -= arr[start]
            start += 1

        # Check if sum matches target
        if curr_sum == target:
            return [start + 1, end + 1]

arr=[1, 2, 3, 7, 5]
target = 12
print(subarraySum(arr,target))

# without function
lst=[1, 2, 3, 7, 5]
target = 12
start=0
current_sum=0

for i in range(len(lst)):
    current_sum+=lst[i]
    if current_sum>target:
        current_sum-=lst[start]
        start+=1

    if current_sum==target:
        print([start+1,i+1])

# missing number
lst=[1,2,4,6,7,8,9,10]
missing=[]
for i in range(len(lst)-1):
    if lst[i+1]-lst[i]>1:
       for num in range(lst[i]+1,lst[i+1]):
           missing.append(num)
print(missing)
