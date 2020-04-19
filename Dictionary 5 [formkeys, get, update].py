#;==========================================
#; Title:  Python Dictionary 5
#; Author: @AyemunHossain
#;==========================================


#fromkeys method

#creating dictionary by fromkeys

keys = [1,2,3,4,5]
my_dict = dict.fromkeys(keys) 	#initialize with none
print(my_dict)

my_dict = dict.fromkeys(keys,0) #initialize with 0 'zero'
print(my_dict)

info_dict={}.fromkeys(['Name','Job','Address','University'],'Unknown')
print(info_dict)

#get method
info = {'Name' : 'Jhon', 'Job':'IT','Address': 'New yourk City','University': 'DIU'}
print(info.get('Name'))


#update method 
info.update({'Name' : 'Aronno', 'Address': 'Faridgonj'})
print(info)

one = {}
#any method 
print(any(info)) #returns true if any of dict value is true
print(any(one))