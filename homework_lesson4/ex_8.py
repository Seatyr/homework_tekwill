"""
Scrieți un program care cere utilizatorului să introducă o propoziție.
Dacă propoziția se încheie cu un semn de întrebare ("?"),
afișați mesajul „Aceasta este o întrebare”.
În caz contrar, afișați mesajul „Aceasta nu este o întrebare”
"""
prop = str(input('Introduceti o "Propozite": '))
if '?' == prop[-1]:
    print('Aceasta propozitie este o intrebare')
else:
    print('Aceasta propozitie nu este o intrebare')