#Advance problem : 


#if you have a list and it's have multiple stage of address then how can you added those item in a addresss 

st_info=['Ashik','Permanent addres : Dhanmondi ,Dhaka','Present Address : Dhanmondi ','Gardian Address: Uttora, Dhaka','Daffodil International University']
name,*address,university = st_info

print(name)
print(address)
print(university)

#if you need the name from this list then :
name = st_info[0]                                       #noobs way :))
name,*_ = st_info                                       #pro way :Yo
print(name)

_,*add,_ = st_info                                       #Only pythonian's understand this
print(add)

#..........>>> Mapping method with list
girlfriend_list=['Asifia','Ahia','Nadia','Paria','Tamannna']

def fun(girl):
    return(f"I Love You {girl}") 
    
ILV = map(fun,girlfriend_list)                          #Hashtag Playboy :))
print(list(ILV))                                        #Say with print

#.............>>> Filter method with list and function : 
def even_nums(i):
    if i % 2 == 0:
        return True
    else:
        return False

Number_list=[0,1,2,3,4,5,6,7,8,9,10,14,12,14,15,17,18,19,21,23]
even_nums=filter(even_nums,Number_list)
print(list(even_nums))

#same things lambda apporach

even_list = filter(lambda x: x % 2 == 0, Number_list)
print(list(even_list))


#.............>>> Lets see enumerate method :  enumerate(iter,start_index)  will return (index,item)
student_list=["Khalid","Ashik","Alif","Khalid","Atif","Ayemun","Billie","Alif","Atif","Eilish","Khalid"]

indexed_list = list(enumerate(student_list,0))
print(indexed_list[0][1])                                   #You can access the name in this order


#............>>> Reduce method : 
import functools

lis = [ 10 , 3, 5, 6, 2] 
print(functools.reduce(lambda a,b: a+b,lis))                #Sum of the list 
print(functools.reduce(lambda a,b: a if a>b else b ,lis))   #bigest elements of list
print(functools.reduce(lambda a,b: a if a<b else b ,lis))   #smallest elements of list


#..................>> chain method <<<.............
from itertools import chain
list1 = [1, 3, 4, 5] 
list2 = [6, 7, 8, 9, 10] 
list3 = [11, 12, 13, 14, 15, 16] 

final_list=list(chain(list1,list2,list3))
print(f"The Final List : {final_list}")

