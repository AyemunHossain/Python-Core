#;==========================================
#; Title:  Python list part 4
#; Author: @AyemunHossain
#;==========================================

#Let's check if the list if that contained our desired item

student_list=["Khalid","Ashik","Alif","Khalid","Atif","Ayemun","Billie",
                "Alif","Atif","Eilish","Khalid"]

print("Khalid" in student_list)

#Let's check that items index 
print(f"The khalid index is : {student_list.index('Atif')}")

#Let's count the quantity of any particular item

print(f"The item 'Khalid' contains {student_list.count('Khalid')} times")
print(f"The item 'Ashik' contains {student_list.count('Ashik')} times")

#If we want to revarse any list then:

demo_list = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
demo_list.reverse()     #Note it will revarse the main list
print(f"The revarsed list :- {demo_list}")


#If we sort any unsorted list then : <Assending Order>
garbage_list = [4,2,0,15,3,14,5,7,13,8,16,10,11,9,6,1,12]
garbage_list.sort()
print(f"The sorted list is :- {garbage_list}")

#but if you want sort any unsorted list in <descending order>
list1 = [4,2,0,15,3,14,5,7,13,8,16,10,11,9,6,1,12]
list1.sort(reverse=True)
print(f"The Desending order sorted list :- {list1}")

#....Range method in list creation:
new_list = list(range(0,11))
print(f"New Created list : {new_list}")

print(f"New Created list 2 : {list(range(5,-1,-1))}")

#Join with list .......BASE_STRING.JOIN(ITERABLE ITEMS)
words=['Coding','Is','Fun!']
print(" ".join(words))


#.........>>> List slicing <<<............#
student_list=["Khalid","Ashik","Alif","Samir","Atif","nAyemun HossainI","Billie","Alif","David"]
print(student_list[0:])     #Print index zero to end
print(student_list[1:])     #Print index one to the end 
print(student_list[2:6])    #print index TWO to SIX 

print(student_list[::2])    #print index zero to end in step two

#You can simply revarse the list with slicing
print(student_list[::-1])

#...........> Advance list slicing stuff
#You can also slice a particular index 
print(student_list[5][1:len(student_list[5])-1:1])

#you can slice string also like this : 
print("Ashik"[0])
print("Ayemun"[0:6:])
print("AAASSSHHHIIIKKK"[0::3])

#Appending list by slicing 
numbers = [1,2,3,4,5,6,7,8,9]
numbers[len(numbers):len(numbers)]=[10]
print(numbers)

#Extending list by slicing 
numbers=[10,11,12,13,14,15]
numbers[0:0] = [1,2,3,4,5,6,7,8,9]
print(numbers)

#Actually this is more than Extending : you can say advance extending
#In extend what you can only do is appned a whole list at end 
#But with list slicing you can add secondary list in any index you actually want to 

numbers=[10,11,12,13,14,15]
numbers[4:4] = [1,2,3,4,5,6,7,8,9]      #In forth index
print(numbers)
