names = ['John', 'Jane', 'Jim']
marks = [80, 90, 85]
new_dict={}
for i in range(len(names)):
    new_dict.names[i]=marks[i]
print(new_dict)

original = {'one': 1, 'two': 2}
new_dict = {}

for key in original:
    new_dict[key.upper()] = original[key]

print("Modified keys:", new_dict)

def remove_duplicates(lst):
    result=[]
    for item in lst:
        if item not in result:
            result.append(item)
    return result

lst = [1, 2, 4, 4, 5, 5, 6]
unique_lst=remove_duplicates(lst)
print(unique_lst)

lst=[1,2,4,4,5,5,6]
result=[]
for item in lst:
    if item not in result:
        remove_duplicates=result.append(item)
        a=lst.sort()
print(lst)
print(result)
