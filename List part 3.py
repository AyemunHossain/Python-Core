#;==========================================
#; Title:  Python list part 3
#; Author: @AyemunHossain
#;==========================================



#There another Advanced method add multiple list into a list it's from ---:itertools
from itertools import chain
list1 = [1, 3, 4, 5] 
list2 = [6, 7, 8, 9, 10] 
list3 = [11, 12, 13, 14, 15, 16] 

final_list=list(chain(list1,list2,list3))
print(f"The Final List : {final_list}")


#........... >>>If you want to add any item to an specific index <<........#
numbers = [1,2,4,5]  #....3 is missing
numbers.insert(2, 3)
print(numbers)

#Add multiple item in multiple index
numbers.insert(5,6)
numbers.insert(6,7)
numbers.insert(7,8)
numbers.insert(8,9)
numbers.insert(9,10)

print(f"Number List : {numbers}")



# .............. > let's see how to remove items form list ...........#

demo_list = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

#......remove method list.remove(item)

demo_list.remove(5)
print(demo_list)

demo_list.remove(6)
demo_list.remove(7)

print(demo_list)

#....pop method list.pop(index)

demo_list.pop(0)
print(demo_list)

demo_list.pop(3)
demo_list.pop(4)

print(demo_list)
#you will see here a fact when you pop index 0 then index 1 will become 0 after then things goes like that