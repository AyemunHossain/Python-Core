#;==========================================
#; Title:  Python Dictionary 1
#; Author: @AyemunHossain
#;==========================================


#Declaring Dictionary ......
#Way: 1 
a = dict([("Ashik",2408),("Asif",2333),("Alif",2322)])
print(a)

#way : 2 

b = {"Ashik":2408,"Asif":2333,"Alif":2322}
print(b)

#Way : 3

opps_dictionary=dict(name='Ashik',age=20,job="Student")	#you can use sting key without "" or '' ...hashtag i love python :)
print(opps_dictionary)

#Way : 4 
#Declaring by iteration
iter_dict = {x:x*x for x in range(10)}	# hastag i know you don't like this way :))
print(iter_dict)


#Declaring Empty dictionary
empty_dictionay={}
print(empty_dictionay)



#creating DICTIONARY with int and string both key
mix_dict={1:'Carrots','Onion':'Expensive','Ginger':'Not needed',2:'Potato'}
print(mix_dict)
