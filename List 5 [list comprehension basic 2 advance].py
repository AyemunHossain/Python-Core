#;==========================================
#; Title:  Python list part 5
#; Author: @AyemunHossain
#;==========================================

#...............>>> List Comprehension <<<..................#
nums=[1,2,3,4,5]
multi_nums=[i*10 for i in nums]     #or you can actullly create any list with list comprehension
print(multi_nums)

print([i*10 for i in nums])

friends=['ashik','eyasin','rashed','siam','santo']
[print(name) for name in friends]

#...........You can use if elif else in list comprehension
even_number_list=[i for i in range(0,15) if i%2==0]
print(even_number_list)
odd_number_list=[i for i in range(0,15) if not i%2 ==0]
print(odd_number_list)

#lets make a bool list with list comprehension
simple_list=[0,[],"Ashik",'',5] 
bool_simple_list=[bool(check) for check in simple_list]     #it will return false for 0 and Null 
print(bool_simple_list)

#..........Let's use list comprehension for TYPE CASTING
int_list=[1,2,3,4,5,6,7,8,9]
print(f"Before conversion : {int_list[0]} is the type of {type(int_list[0])}")
str_list=[str(i) for i in int_list]
print(str_list)
print(f"After conversion : {str_list[0]} is the type of {type(str_list[0])}")

simple_list=[1,2,3,4,5,6,7,8,9]
simple_list=[str(i)+"A" for i in simple_list]
print(simple_list)

#..........Let's use list comprehension for printing multi dimesional list
multi_dimensional_list=[[12.3,13.6,14.9],[17.6,17.7,17.8,17.9]]

#print without list comprehension :
for items in multi_dimensional_list:
    for item in items:
        print(item)

#with list comprehension is : 
[[print(item) for item in items]for items in multi_dimensional_list]


#Lets see some real_life example for list comprehension 
users=[
    {'user_name': 'Ashik', 'tweets': ['I love to tweet','It\'s getting so hard to move on  ']},
    {'user_name': 'Asif', 'tweets': ['Love you anddy ','Petter don\'t push me over her']},
    {'user_name': 'Akik', 'tweets': []},
    {'user_name': 'Atif', 'tweets': ['My First Tweet','Love the Avenger End Game']},
    {'user_name': 'Alif', 'tweets': []},
]
upper_name_of_active_user=[user['user_name'].upper() for user in users if user['tweets']]
upper_name_of_inactive_user=[user['user_name'].upper() for user in users if not user['tweets']]

print(f'Active Users :  {upper_name_of_active_user}\nInactive Users : {upper_name_of_inactive_user}')

#You can use list for initializing variable
name,address,university=['Alif','Chandpur','DIU']
print(name,address,university)