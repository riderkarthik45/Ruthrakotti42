text=input("Enter to write some in file")
x=open('15minstask.txt','w')
x.write(text)
x.close()

import smtplib

sender_email = "ruthrakotti777@gmail.com"
password = "ntvndudyompuleeo"
to_email = "veera4012@gmail.com"
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender_email, password)
print("login successful")
server.sendmail(sender_email,to_email,text)
print("email sent to ",to_email)
server.quit()

print("hello")
print("hai")