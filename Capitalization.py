#Just simple capitalize
name=["ashik"]
Name=[name[0][0].upper()+name[0][1:]]
Name=str(Name[0])
print(Name)

#user inputed data capitalize
user_inputed_name="ayemun hossain"
name_list=[word[0].upper()+word[1:] for word in user_inputed_name.split()]
name=" ".join(name_list)
print(name)

#user inputed data capitalize : 2 <complex>
user_inputed_name="AyEmun hosSaiN"
name_list=[word[0].upper()+word[1:].lower() for word in user_inputed_name.split()]
name=" ".join(name_list)
print(name)
