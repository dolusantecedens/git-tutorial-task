def check(string):
    if string[::-1]!=string: #sprawdzenie stringa z odbiciem lustrzanym
        return False        #zwraca falsz jesli warunek nie spelniony
    else:
        return True
print(check(input('podaj fraze do sprawdzenia')))