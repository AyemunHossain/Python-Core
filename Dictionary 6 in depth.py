#;==========================================
#; Title:  Python Dictionary 6
#; Author: @AyemunHossain
#;==========================================



#Geting more depth with dictionary 

str1="ABCDEFGH"
str2="12345678"
combo={str1[i]: str2[i] for i in range(0,len(str1))}
print(combo)

st_name=['Ashik','Asif','Alif','Atif','Afif','Musleh','Eyasin']
st_id=['55','79','78','88','66','44','555']

st={st_id[i] : st_name[i] for i in range(0,7)}
print("Id      Name: ")
[print(f"{x} ---  {y}") for x,y in st.items()]


#get method with default value
dict = {'Name': 'Zabra', 'Age': 7}
print(f"Value : {dict.get('Education','Not Found')}")


#setdefault() method


person = {'name': 'Phill', 'age': 22}
age = person.setdefault('age')  #when key is in dict
print('person = ',person)

person = {'name': 'Phill'}	# key is not in the dictionary
salary = person.setdefault('salary')
print('person = ',person)


#You can  update a DICTIONARY with copy a whole DICTIONARY 
demo1 = {'Name' : 'Jhon', 'Job':['IT','Ethical Hacking','Developing'],'Address': 'New yourk City','University': 'DIU'}
demo2= {'Name' : 'Ashik', 'Job':'Business','Address': 'Dhaka','University': 'VUGICHUGI'}
demo1.update(demo2)	#This is when all key matches 
print(demo1)

#if keys are not matching then?? it will added them in update dict

d1 = {'Name' : 'Jhon'}
d1.update(demo2)
print(d1)