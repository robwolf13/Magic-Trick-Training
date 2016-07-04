__author__ = 'Robert Woolley'

'''Trains a set of mental maths magic questions'''

#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import random
def mainloop():
   k = random.randrange(1,100)
   #squaring a number by the difference of two squares
   if input ("What is "+str(k)+" squared?") != "n":
      print (k*k)
   n = random.randrange(1,100)
   #cube rooting by unique mapping
   if input ("What is the cube root of "+str(n**3)) != "n":
      print (n)
   l = random.randrange(7,10)
   print (l)
   m = []
   t = 0
   for i in range(l-1):
      k  = random.randrange(1,10)
      m += [k]
      t += k
   print (m)
   #finding the missing number of a 7-10 digit number with was made by multiplying 1 digit numbers
   if input ("What is the missing number?")!="n":
       print (9 - t%9)
   if input ("again?;") != "n":
       mainloop()
mainloop()
