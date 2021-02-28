# Reverse the list using for loop
# num1 = [5, 15, 20, 25, 30]
    
num1 = [5, 15, 20, 25, 30]
num2 = []

for i in range(len(num1)-1, -1, -1):
    num2.append(num1[i])

print("Original array:",num1)    
print("Array in reverse order:",num2)