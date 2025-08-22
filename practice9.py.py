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
