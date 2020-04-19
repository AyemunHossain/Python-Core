#;==========================================
#; Title:  Python Dictionary 3
#; Author: @AyemunHossain
#;==========================================



#Adding a list in a dictionary 
order={1:'Carrots',2:['Onion','Ginger','Potato']}
print(order)

student_info = {'name':['Ayemun','Hossain'],'id':1408,"cgpa":[3.33,3.45,4.00,3.44,3.56,2.52]}
print(student_info)

#Print these items
for key,items in student_info.items():
	if type(items) == list:
		print(f"{key}  :",end='')
		for i in items:
			print(i,end=', ')
		print('')
	else:
		print(f"{key}  : {items}")



#Add new item in DICTIONARY 
student_info["semester"]=['Spring-2019','Summer-2019','Fall-2019','Spring-2020']
#printing dict again
for key,items in student_info.items():
	if type(items) == list:
		print(f"{key}  :",end='')
		for i in items:
			print(i,end=', ')
		print('')
	else:
		print(f"{key}  : {items}")

#Access the key list:
print(f"The First semester is : {student_info['semester'][0]}")


#Check the dictionary if it contain a certain key: return true if found 
print('name' in student_info)
print('address' in student_info)

#let's check any value contains in dictionary value 
print(1408 in student_info.values())
print('Ashik' in student_info.values())