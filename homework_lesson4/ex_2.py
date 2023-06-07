"""
Citiţi de la tastatură 2 valori.
Verificaţi dacă ele sunt egale sau nu şi afişaţi la ecran.
"""
var1 = input('Tastati prima valoare: ')
var2 = input('Tastati a doua valoare: ')
egale = var1 == var2
if egale == True:
    print('Sunt Egale')
else:
    print('Nu sunt Egale')