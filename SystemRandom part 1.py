#;==========================================
#; Title:  System Random Module
#; Author: @AyemunHossain
#;==========================================

import random as r 
#Cryptographically Secured Randmon Module

sr=r.SystemRandom()
sr.seed()

#Now sr is the instance of SystemRandom And you can use any kind of methods 
#That's works in random module and will be cryptographically secure 


#Crypthographically Secure Random Float number: 
randomFoat=sr.uniform(10,15)
print(round(randomFoat,5))


#Crypthographically Secure Random ascci <lower and upper>
import string
word = string.ascii_letters
secure_word = "".join(sr.choices(word,k=5))
print(secure_word)


#Crypthographically Secure Random ascci letter and numbers:
w_n = string.ascii_letters+string.digits
secure_w_n = "".join(sr.choices(w_n,k=10))
print(secure_w_n)

#let's make uniqe that will be more secure:
more_wn = string.ascii_letters+string.digits
secure_more_wn = "".join(sr.sample(more_wn,k=25))
print(secure_more_wn)

#Even more strong combinaton with : 

mixed = string.ascii_letters+string.digits+string.punctuation
secure_mixed = "".join(sr.sample(mixed,k=30))
print(secure_mixed)