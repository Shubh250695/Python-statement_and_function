# define a list, display numbers which are divisible by 4 and
# if you find number greater than 120 come out of the loop.
# list1 = [8, 15, 32, 42, 60, 75, 122, 132, 150, 180, 190]

list1 = [8, 15, 32, 42, 60, 75, 122, 132, 150, 180, 190]
print ("List =",list1)

list2 = []

for i in range(0,len(list1)):
    if list1[i]<120 and list1[i] % 4 == 0 :
        list2.append(list1[i])

print("Numbers that are divisible by 4 and greater than 120 : ",list2)