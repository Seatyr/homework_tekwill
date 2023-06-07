"""
Scrieți un program care cere utilizatorului să introducă o parolă.
Dacă parola conține cel puțin 8 caractere și include atât litere mari,
cât și litere mici, afișați mesajul „Parolă puternică”.
În caz contrar, afișați mesajul „Parolă slabă”.
"""
user = input('Introduceti un Username: ')
password = input(f'Salut {user} introduceti va rog o parola: ')
if len(password) >= 8 and any(litera.isupper() for litera in password) and any(litera.islower() for litera in password):
    print('Parola puternica')
else:
    print('Parola slaba')
# Am gasit asa varianta pe Internet 'any(litera.isupper() for litera in password) and any(litera.islower() for litera in password)'
# Dar noi nu am invatat functia "ANY" sau poate eu nu am fost atent care are fi varianta correcta din pucntul tau de vedere