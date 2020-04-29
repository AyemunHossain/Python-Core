#;==========================================
#; Title:  File handeling part 1
#; Author: @AyemunHossain
#;==========================================


#Read a file : 
file = open("story.txt","r")
containt=file.read()
file.close()
print(containt)

#read file line by line : 
file=open("story.txt","r")
[print(i,end="") for i in file]
file.close()

#Read specific amount of bit :
file = open("story.txt","r")
content=file.read(10)
file.close()
print(content)

#write a file : 
file=open("story2.txt","w")
file.write("This story is about the boy who live.\nHis name is Harry Potter.\n")
file.close()

#check out that file 
file = open("story2.txt","r")
content=file.read()
file.close()
print(content)

#append a file 
file=open("story2.txt","a+")
file.write("The boy was cursed by \"Voldemort\".\n")
file.close()
file = open("story2.txt","r")
content=file.read()
file.close()
print(content)

#append a file and read:
file=open("story2.txt","a+")
file.write("\"Voldemort\" Killed Harry's parents.\n")
file.seek(0)
content=file.read()
print(content)

#Print the actual file name : 
f=open("story2.txt",'r')
print(f.name)
f.close()
