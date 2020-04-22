#;==========================================
#; Title:  Python Random module part 3
#; Author: @AyemunHossain
#;==========================================
import random as r 


#whole random module is controled by seed value 
r.seed(0)
print(r.randint(0,500))
r.seed(0)
print(r.randint(0,500))
r.seed() 
###let's shuffling a string
name="ashik"
l_n=list(name)
r.shuffle(l_n)
name=''.join(l_n)
print(name)
#shuffle second time 
l_n=list(name)
r.shuffle(l_n)
name=''.join(l_n)
print(name)


#let's control shuffling by seed 
name="ashik"
l_n=list(name)
r.seed(0)
r.shuffle(l_n)
name=''.join(l_n)
print(name)

name="ashik"
l_n=list(name)
r.seed(0)
r.shuffle(l_n)
name=''.join(l_n)
print(name)
r.seed() 


#note: you can actually do the shuffle with the help of sample
lis=[1,2,3,4,5]
r.seed()  #when you need to clear seed value from others then just type it : 
look_like_shuffle=r.sample(lis,len(lis))
print(look_like_shuffle)

#shuffle two python list at once with same order : 
empName = ['Jhon', 'Emma', 'Kelly', 'Jason']
empSalary = [7000, 6500, 9000, 10000]
suf_both=list(zip(empName,empSalary))
r.shuffle(suf_both)
s_name,s_salary=zip(*suf_both)
s_name,s_salary=list(s_name),list(s_salary)
print(s_name,s_salary)

#generate random float number with nth of precision
print(round(r.uniform(0.1,5.0),5))
print(round(r.uniform(0.1,5.0),3))
print(round(r.uniform(0.1,5.0),9))