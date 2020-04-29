#;==========================================
#; Title:  System Random Module part 2
#; Author: @AyemunHossain
#;==========================================

#Get more specific character if we want 

import random as rn 
sr = rn.SystemRandom()
import string
sr.seed()

#Secure Random Lower Case Ascii Character
lower_ascci = string.ascii_lowercase
safe_lower = "".join(sr.sample(lower_ascci,k=5))
print(safe_lower)

#Secure Random Upper Case Ascii Character
upper = string.ascii_uppercase
safe_upper = "".join(sr.sample(upper,k=5))
print(safe_upper)

#Task : ONE 
#->Generate a ten-character password with 
	#one lowercase character
	#one uppercase characteR
	#one digits 
	#one special character.

rand_sor=string.ascii_letters+string.digits+string.punctuation
passo=sr.choice(string.punctuation)
passo+=sr.choice(string.ascii_letters)
passo+=sr.choice(string.digits)
passo+="".join(sr.sample(rand_sor,7))
pass_list = list(passo)
sr.shuffle(pass_list)
print("".join(pass_list))