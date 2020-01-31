#;==========================================
#; Title:  Sum of two numbers by try except case
#; Author: @AyemunHossain
#;==========================================

#Apporach : 1
try : 
    a = int(input())
    b = int(input())
except:
    print("You have to enter numbers")
else:
    print(f"The sum of {a} and {b} is : {a + b}")


#Apporach : 2
try : 
    a = int(input())
    b = int(input())
except ValueError  as VL:
    print(f"You have to enter numbers :  {VL}")
else:
    print(f"The sum of {a} and {b} is : {a + b}")

#Apporach : 3
try :
    a = int(input())
    b = int(input())
except ValueError:
    raise ValueError(f"You have to input Numbers")
else:
    print(f"The sum of {a} and {b} is : {a+b}")
