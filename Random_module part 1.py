#;==========================================
#; Title:  Python Random module part 1
#; Author: @AyemunHossain
#;==========================================


import random as r 

#random integer
print(r.randint(1,100))
print(r.randint(1,100))
print(r.randint(1,100))

#randrange
print(r.randrange(10,100,5))
print(r.randrange(10,100,5))
print(r.randrange(10,100,5))

#random floating numbers
print(r.random())
print(r.random())

#random floating within given range
print(r.uniform(5,10))
print(r.uniform(5,10))
print(r.uniform(5,10))

#random.choice() example 

list_1=[1,2,3,4,5,6,7,8,9]

print(r.choice(list_1))    #This choice is not cryptographically secured 
print(r.choice(list_1)) 
print(r.choice(list_1)) 

#choice in dictionary
dictt={
  "Kelly": 50,
  "Red": 68,
  "Jhon": 70,
  "Emma" :40
}

key=r.choice(list(dictt))
value=dictt[key]
print(f"{key} : {value}")


#let's chose same element every time : by help of seed method
print("Now we are selecting the same element everytime : ")
r.seed(4)
key=r.choice(list(dictt))
value=dictt[key]
print(f"1 - {key} : {value}")

r.seed(4)
key=r.choice(list(dictt))
value=dictt[key]
print(f"2 - {key} : {value}")

r.seed(4)
key=r.choice(list(dictt))
value=dictt[key]
print(f"3 - {key} : {value}")

r.seed(4)
key=r.choice(list(dictt))
value=dictt[key]
print(f"4 - {key} : {value}")