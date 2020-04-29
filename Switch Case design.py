def switch(a):
    switcher={
        1:'Ashik',
        2:'Malak',
        3:'Ahiya',
	4:'Amina',
	5:'Rafik',
	6:'Habib'
        }
    return switcher.get(a,"Not Found")


print(switch(1)) #on you condition call the function with value