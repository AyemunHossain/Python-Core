
def refomer(operator,x,y):
	x=str(x)
	y=str(y)

	x=x.replace(" ","")
	y=y.replace(" ","")
	try:
		x = int(x)
		y = int(y)
	except:
		x = float(x)
		y = float(y)
	finally:
		value = calculator(str(operator),x,y)

	return x,y,value;

def calculator(operator,x,y):
    return {
        '+': lambda : x+y,
        '-': lambda : x-y,
        '*': lambda : x*y,
        '/': lambda : x/y,
    }.get(operator,"Not Available")()


strr=input("Enter the expresion <x+y>: ")
op = ['+','-','*','/']
count = 0
for num in strr:
	if num in op:
		opee = num
		count+=1
	if count>1:
		break;

if count==1:
	try:
		x,y=strr.split(f'{opee}')
	except:
		print("Wrong Formated value: input <x+y> format")
	else:
		x,y,val= refomer(opee,x,y)
		print(f"{x} {opee} {y} = {val}")

