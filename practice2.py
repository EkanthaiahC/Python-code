numbers = [20, 55, 80, 30]
count = 0
for num in numbers:
    if num > 50:
        count += 1
print("Count:", count)

students=['ram','sitha','abhi']
for i in range (len(students)):
    students[i]=students[i]+"- students"
print(students)

students=['ram','sitha','abhi']
for i in range(len(students)):
    students[i]=students[i].upper()
print(students)

numbers = [10, -5, 7, -3, 12]
result=[]
for num in numbers:
    if num>=0:
        result.append(num)
print(result)