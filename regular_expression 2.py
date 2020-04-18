import re 



#Search for the first white-space character in the string:
txt = "I am a Bangladeshi"
r =re.search("\s",txt)

print(f"The index of first space is : {r.start()}")

#Split the string by Space
print(re.split("\s",txt))

#You can control the spliting by the maxsplit parameter
print(re.split("\s",txt,2))

#re have replacing lib : sub
print(re.sub("\s","_",txt))

#You can define the number of replaceing by count parameter
print(re.sub("\s","_",txt,2))

#Search for an upper case "A" character in the beginning of a word, and print its position:
txt = "i so lonely broken Angel"
print(re.search(r"\bA",txt).start())

#let's see how we can also see see the ending postion of that word
print(re.search(r"\bA\w+",txt).span())

#printing the matching string as sting 
print(re.search(r"\bA\w+",txt).string)