list_length=0
print('prezentuje liste zakupow')
list={'piekarnia':['Chleb', 'Pączek', 'Bułki'], 'warzywniak':['marchew','seler','rukola']}
for i in list:
    print('Idę do  %s, i kupuje %s :'%(i.capitalize(),list[i]))
    list_length+=len(list[i])
print('kupujesz %i produktów' %(list_length))