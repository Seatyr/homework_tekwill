"""
Scrieţi un program care verifică dacă litera "a" se află pe a 2-a poziţie într-un String citit de la tastatură.
"""
sir = str(input('Introduceti un sir de caractere: '))
if 'a' == sir[1]:
    print('Litera "a" este prezenta pe a 2-a pozitie')
else:
    print('Litera "a" nu este prezenta pe a 2-a pozitie')