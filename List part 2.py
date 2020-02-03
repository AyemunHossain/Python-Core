#;==========================================
#; Title:  Python list part 2
#; Author: @AyemunHossain
#;==========================================

numbers = [1,2,3,4,5,6,7,8,9]
alphabets = ['a','b','c','d','e','f']

#You can check the length
print(len(numbers))
print(len(alphabets))

# you can print those index that you want to ---list[from : to]
print(numbers[2:5])
print(alphabets[3:6])

#..........Iterating over list...............

for number in numbers:
    print(number,end=' ')
print('')

index=0
while (index<len(alphabets)):
    print(alphabets[index],end=' ')
    index+=1
print('')

#...........>> You can appned a whole list to another existing list <<...........

n1 = [0,1,2,3,4,5]
n2= [6,7,8,9,10]

n1.append(n2)
print(n1)
#After printing this list you may find a problem here :[0, 1, 2, 3, 4, 5, [6, 7, 8, 9, 10]]
#What if we want them in a single list not multi dimensional list : so you need to use list1.extend(list2)

num1 = [0,1,2,3,4,5]
num2= [6,7,8,9,10]

num1.extend(num2)
print(num1)