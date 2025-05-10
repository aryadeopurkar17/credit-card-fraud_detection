import os,math
import random,sys
import smtplib
mailid="sangitahazra612@gmail.com"
digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
msg='Your OTP Verification for app is '+OTP+' Note..  Please enter otp within 2 minutes and 3 attempts, otherwise it becomes invalid'
file2=open("otp.txt","w")
file2.write(OTP)
file2.close()

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("hsangitaa@gmail.com", "Sangu123")
print(msg)
s.sendmail("hsangitaa@gmail.com",mailid,msg)

os.system('python Second.py')