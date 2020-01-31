#;==========================================
#; Title:  Print Hello World
#; Author: @AyemunHossain
#;==========================================

import math 

#Apporach : 1
a = float(input("Enter a number: "))
sq = math.sqrt(a)

print(f"Squre root of {a} : {sq}")



#Apporach : 2
try:
    a = float(input("Enter a number: "))
except ValueError:
    raise ValueError("Input must be real number")
else:
    sq = math.sqrt(a)
    print(f"Squre root of {a} : {round(sq,3)}")
