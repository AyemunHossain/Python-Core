#;==========================================
#; Title:  System Random Module part 3
#; Author: @AyemunHossain
#;==========================================
import string

#secrets modules to generate the cryptographically secured data
import secrets
sec_rand = secrets.SystemRandom()

flt = sec_rand.uniform(0,10)
print(round(flt,3))

print(f"Random Number bellow 10 : {secrets.randbelow(10)}")

#Secure unsigned integer with k random bits.
print(f"Secure unsigned integer {secrets.randbits(k=10)}")


#Generate a secure string with secret modules :
print(f"Secure string -{secrets.token_bytes(32)}")

print(f"Secure sting <hex format>: {secrets.token_hex(32)}")


#Secret Choices:
password = "".join(sec_rand.choices(string.ascii_letters+string.digits+string.digits,k=8))
print(password)


#Secure token for Passwords,OTP,session keys,Password changing,registration confirm,etc: 
print(f"URL : https://adobil.com/user/ashik001/reset={secrets.token_urlsafe(96)}")
