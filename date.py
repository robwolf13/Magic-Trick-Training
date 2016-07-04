'''Program to train calculating which day of the week a person is born on'''

import random
monthcode = {1:6,2:2,3:2,4:5,5:0,6:3,7:5,8:1,9:4,10:6,11:2,12:4}
days = ["Sun","Mon","Tues","Wed","Thur","Fri","Sat"]
#randomdate
def rdate():
   d = random.randrange(28)+1
   m = random.randrange(12)+1
   y = random.randrange(1900,2050)+1
   print (str(d)+"/"+str(m)+"/"+str(y))
   k = input("new one=n, check = enter:")
   if k == 'n':
       rdate()
   else :
       cday(y,m,d)
#calculate the day for the date
def cday(y,m,d):
   daycode = (d + (y%100) + ((y%100)//4) + monthcode[m])%7
   if (y%4==0)&(m<3):
       daycode = (daycode + 6)%7
   if y < 2000:
       daycode = (daycode + 1)%7
#give you part of the calculation so if a mistake is made by me I can figure out what it was
   print (str(d%7)+"+"+str(monthcode[m])+"+"+str(((y%100)+((y%100)//4))%7)+"="+str(daycode)+"  "+days[daycode])
   k = input("new one=enter, check = c:")

   if k == 'c':
       cday(y,m,d)
   else:
       rdate()
rdate()
