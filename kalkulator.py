import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def summ(a,b,):
    logging.info("Dodaję: %i i %i"%(a,b))
    logging.info("Wynik to: %i"%(a+b))
def subs(a,b):
    logging.info('odejmuje: %i i %i'%(a,b))
    logging.info('wynik to:%i'%(a-b))
def multi(a,b,):
    logging.info('mnoze: %i i %i'%(a,b))
    logging.info('wynik to %i'%(a*b))
def division(a,b):
    logging.info('dziele: %i i %i:'%(a,b))
    logging.info('wynik to %i'%(a/b))
z=int(input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: '))
x=int(input('Podaj składnik'))
y=int(input('Podaj składnik'))
if z==1:
    (summ(x,y))
elif z==2:
    subs(x,y)
elif z==3:
    multi(x,y)
elif z==4:
    division(x,y)
else: 
    print('bledna wartosc')

