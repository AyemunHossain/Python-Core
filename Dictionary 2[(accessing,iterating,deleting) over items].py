#;==========================================
#; Title:  Python Dictionary 2
#; Author: @AyemunHossain
#;==========================================



#Access to the DICTIONARY items : 
new_dict={'Name': 'Ashik', 'Id': 2408, 'Depertment':'SWE'}
print(new_dict['Name'])

#lets see another apporach to do the same things
a='Name'
print(new_dict[a])

#print all the values of dictionary 
print(new_dict.values())

#print all the keys of dictionary 
print(new_dict.keys())

#print all the keys and values of dictionary 
print(new_dict.items())


#Modify the values of dictonary
new_dict['Name']="Rami"
new_dict['Id']=2429
print(new_dict)


#Let's iterate over dictionary 

for key,value in new_dict.items():
	print(f"{key} : {value}")


#List comprehension in dictionary
[print(f"{key} : {value}") for key,value in new_dict.items()]

#Pop any value 
new_dict.pop('Id')
print(new_dict)

#Delete a particular item:
del new_dict['Name']
print(new_dict)

#clearing all items 
new_dict.clear()
print(new_dict)

#Delete the whole dictionary:
del new_dict
print(new_dict)    	#Here you will have a NameError because nothing is exist called new_dict
