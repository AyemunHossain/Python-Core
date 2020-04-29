#;==========================================
#; Title:  File handeling part 2
#; Author: @AyemunHossain
#;==========================================


#Iterate the file line by line

f=open("story2.txt",'r')
[print(i,end="") for i in f]
f.close()


#Read file and storing as list of lines 
file = open("story2.txt","r")

data_list = file.readlines()
file.close()
print(data_list)

#mode function in file :
file = open("story2.txt","r")

if file.mode == 'r':
	print("File is open as read mode")
elif file.mode == 'w':
	print("File is open as write mode")
elif file.mode == 'a+':
	print("Fil is open as append mode")


#try case on file opening 

try : 
    f=open("secret_password.txt", "r")
except:
    print("File is not exist ")
else : 
    pass #further process will done here 
finally:
    print("__Done__")

string_list = ["I","am","Ashik.","I","read","in","Daffodil","International","University.",]

#Write a sequence to file : 
f = open("demo.txt","w")
f.writelines(' '.join(i for i in string_list))
f.close()

seq=['Hello\n','I am Ashik\n','I read in Daffodil International University\n','I live in Dhanmondi\n']
f=open("info.txt",'w')
f.writelines(seq)
f.close()
#check the file
f=open("info.txt",'r')
print(f.read())
f.close()

#Rename the file name: 
import os
os.rename("demo.txt","Demo.txt")

#Delete the file:
os.remove("Demo.txt")