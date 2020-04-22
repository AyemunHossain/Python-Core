#;==========================================
#; Title:  Python Random module part 2
#; Author: @AyemunHossain
#;==========================================

import random as r 

multi_list=[[1,2,3,4],[5,6,4,2],[6,5,4,8],[9,8,7,441]]
print(r.choice(multi_list))

#multiple choices : 
sample_list=[1,2,3,4,5,6,47,28,76,85,74,78]
print(r.choices(sample_list,k=5))   #5 choices among them

#choose from set : 
set1={20, 35, 45, 65, 82}
print(r.choice(tuple(set1)))	#you need to convert set in tuple

#sample modules : 
sample_list=[1,2,3,4,5,6,47,28,76,85,74,78]
sl=r.sample(sample_list,k=5)    #it will make a sample of k number of element from the sample list 
print(sl)

sample_set={1,2,3,4,5,6,47,28,76,85,74,78}    #lets make a sample from set
print(r.sample(sample_set,k=4)) 

sample_dict = { "Kelly": 50, "Red": 68, "Jhon": 70, "Emma" :40 }
print(r.sample(list(sample_dict),k=3)) 	#return the keys in a sample list

#another way to do this 

dictt={
  "Kelly": 50,
  "Red": 68,
  "Jhon": 70,
  "Emma" :40,
  "Ashik" : 79,
  "Musleh": 99,
  "Lia": 100,
  "Miskat": 66,
  "Jacce": 90
}

print(r.sample(dictt.items(),k=5)) 	#return a list of key and value 

#so what's difference between choice and sample :
#sample makes the random sample of given iter
#choice makes random choice of given iter with repeated value 
#let's seeeeeeeeee
sample_list=[1,2,3,4,5,6,47,28,76,85,74,78]
print(f"Always Unique :          {r.sample(sample_list,k=5)}")
print(f"Some time repeted :      {r.choices(sample_list,k=5)}")
