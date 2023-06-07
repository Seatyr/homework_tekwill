"""
Scrieți un program pentru a citi temperatura de la utilizator și pentru a afișa un mesaj adecvat în funcție de starea temperaturii de mai jos.
Temp -40-(-10) atunci 'Vremea extrem de rece'
Temp -10-0 atunci 'Vremea foarte rece'
Temp 0-10 atunci 'Vreme rece'
Temp 10-20 atunci 'Vreme normala'
Temp 20-30 atunci 'Vreme calda'
Temp 30-40 atunci 'Este foarte cald'
Temp >=40 atunci 'Este extrem de cald'
"""
temperatura = float(input('Introduceti temperatura de afara: '))
if temperatura < -40:
    print('Vremea de afara este extrem de rece')
elif temperatura < -10:
    print('Vremea de afara este foarte rece')
elif temperatura < 0:
    print('Vremea de afara este rece')
elif temperatura < 10:
    print('Vremea de afara este normala')
elif temperatura < 20:
    print('Vremea de afara este calda')
elif temperatura < 30:
    print('Vremea de afara este foarte cald')
else:
    print('Vremea de afara este extrem de cald')