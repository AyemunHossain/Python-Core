#;==========================================
#; Title:  Python Dictionary 4
#; Author: @AyemunHossain
#;==========================================



#let see some DICTIONARY method 

my_dict = {'Name' : 'Jhon', 'Job':['IT','Ethical Hacking','Developing'],'Address': 'New yourk City','University': 'DIU'}

#pop method:
print(my_dict.pop('Job')) #pop will return the poped items
print(my_dict)

#popitem method:
print(my_dict.popitem()) #POP the last index
print(my_dict) 

#copy method:
new_dict = my_dict.copy()
print(new_dict)


#clear method:
new_dict.clear()
print(f"This is cleared DICTIONARY: {new_dict}")


#del method 
my_dict= {'Name' : 'Jhon', 'Job':['IT','Ethical Hacking','Developing'],'Address': 'New yourk City','University': 'DIU'}

del my_dict['Job']
print(my_dict)