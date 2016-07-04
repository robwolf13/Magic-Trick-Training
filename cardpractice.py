__author__ = 'Robert Woolley'

'''Program that spint out either a number between 1-52 or and random playing card
to train an magic trick involving a special deck'''

import random
suits = {0:"clubs",1:"hearts",2:"spades",3:"diamonds"}
cards = {0:"king",1:"ace",11:"jack",12:"queen"}
#random number
def rnumber():
   d = random.randrange(52)+1
   print (d)
   if input("another:")!='n':
       rnumber()
   else:
       rcard()
#randomnumber
def rcard():
   d = random.randrange(52)+1
   s = suits[(d-1)//13]
   c = d % 13
   if c not in range(2,11):
      c = cards[c]
   print("-----------")
   print(c)
   print(s)
   if input("another:")!='n':
       rcard()
   else:
       rnumber()
rnumber()
