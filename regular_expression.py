import re 
#re is the regular expression python lib


#Check if the string has any 'a' characters:
txt = "Ashika"

print(re.findall("[a]",txt))

#Check if the string has any 'aeiou' characters:
txt = "Do the best you know"
print(re.findall("[aeiou]",txt))

#Check if the string has any characters between a and h:
print(re.findall("[a-h]",txt))

#Check if the string has other characters than p,r,m:
txt = "programming is a superpower"
print(re.findall("[^prm]",txt))

#Check if the string has number 01-39 
num = "12"
num2 = "56"

print(re.findall("[0-3][1-9]",num))
print(re.findall("[0-3][1-9]",num2)) #it will show empty which means no matching sequence


#Check if the string has any characters from a to z (lower case)
txt = "A Progrmmer Is Not a Successful At All"
print(re.findall("[a-z]",txt))


#Check if the string has any characters from A to Z (Upper case)
print(re.findall("[A-Z]",txt))


#Check if the string has any characters between a to z and A to Z :
print(re.findall("[a-zA-Z]",txt))
